import sys
import json
import urllib2
import urllib
import re
import math
import collections
from datetime import datetime

from sonification import sonify

r = re.compile("\[sentence:(.*[0-9])\]")

def _parse( line ):
   return map( lambda x: int(x), line.strip().split(',') )

size = 3.0
store = collections.deque(maxlen= size)

def _mood( positive, negative ):
  positive = positive - 1
  negative = negative + 1
  if abs( positive ) > abs( negative ):
    return positive
  else:
    return negative

def analysis( data ):
     store.append( data )
     mood = reduce( lambda x, y : x + y, map( lambda x : _mood( x[1], x[2] ) , store ) )
     weight = reduce( lambda x, y: x+y, map( lambda x : x[3], store ) )
     # delta, mean mood, this mood, mean weight, this weight
     return ( store[-1][0] - store[0][0] , mood / size , _mood( data[1], data[2] ) , weight / size, store[-1][3] )

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
        out.append( datetime.strptime( t , '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%s') )
        out.append( r.search( sentiment.read() ).group(1) )
        out.append( str( len( msg['message'] ) ) )
	sonify( analysis( _parse( ','.join(out) ) ) )

while True:
    line = sys.stdin.readline()
    ## parse the thing as json
    if line != '':
      line = json.loads( line )
      handle( line )
