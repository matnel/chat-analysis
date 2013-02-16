import sys
import json
import urllib2
import urllib
import re
import math
import collections
from datetime import datetime

from sonification import sonify

r = re.compile(".*\[sentence:(.*[0-9])\]")

def _parse( line ):
   return map( lambda x: int(x), line.strip().split(',') )

SIZE = 3.0
store = collections.deque(maxlen= SIZE)

def _mood( positive, negative ):
  positive = positive - 1
  negative = negative + 1
  if abs( positive ) > abs( negative ):
    return positive
  else:
    return negative

def analysis( data ):
  store.append( data )

  size = float( len( store ) )

  mood = reduce( lambda x, y : x + y, map( lambda x : _mood( x[1], x[2] ) , store ) )
  weight = reduce( lambda x, y: x+y, map( lambda x : x[3], store ) )
  voices = len( set( map( lambda x : x[4], store ) ) )
  # delta, mean mood, this mood, mean weight, this weight, number of voices
  return ( store[-1][0] - store[0][0] , mood / size , _mood( data[1], data[2] ) , weight / size, store[-1][3], voices )

def handle( line ):
   if not 'key' in line:
       return
   if line['key'].startswith( 'msgs:' ):
        ## analyze the message lenghts
	msg = line['val'][-1]
        http = 'http://sentistrength.wlv.ac.uk/results.php?' + urllib.urlencode( { 'text' :  msg['message'] } )
	sentiment = urllib2.urlopen( http )
        t =  msg['time']
        out = []
        ## 0 = MOOD
        out.append( datetime.strptime( t , '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%s') )
        ## 1, 2 == SENTIMENT
        out.append( r.search( sentiment.read() ).group(1) )
        ## 3 = message lenght
        out.append( str( len( msg['message'] ) ) )
        ## 4 = voices
        out.append( str( hash( msg['from'] ) ) )
	sonify( analysis( _parse( ','.join(out) ) ) )

while True:
    line = sys.stdin.readline()
    ## parse the thing as json
    if line != '':
      line = json.loads( line )
      handle( line )
