import math
import sys
import datetime

file = open('data', 'a' )

def out( data ):
	print data
	if isinstance(data, list ):
		data = '\n'.join(data)
	file.write( data + '\n' )
	file.flush()

_chord = {
	0 : 'major',
	1 : 'major',
	2 : 'major',
	3 : 'major',
	-1: 'naturalminor',
	-2: 'naturalminor',
	-3: 'naturalminor',
}

def _voices( voices ):
	if voices <= 3:
		return str( voices + 2 )
	if voices < 10:
		return '6'
	return '8'

def _density( mean ):
	## TODO: test more!
	## TODO: check this from empirical logs!
	x = int( mean / 10 ) + 1
	return str( x ) if x < 10 else '10'

previous = datetime.datetime.utcnow()

harmonity = {
-4 : '1',
-3 : '1',
-2 : '1',
-1 : '5',
0 : '5',
1 : '5',
2 : '9',
3 : '9',
4 : '9'
}

def sonify( data ):
   global previous
# delta, mean mood, this mood, mean weight, this weight, voices
   out( [
   		'scaletype ' + _chord[ round( data[1] ) ],
		'harmony ' + harmonity[ round( data[1] ) ],
   		'voices ' + _voices( data[5] ),
   	] )
   previous = datetime.datetime.fromtimestamp( data[0] )

## initial
out( [ 'sound on', 'drums on', 'tempo 100' ] )


## thead for reducing tempo
import time
from threading import Thread

import scipy.stats as stats

def reduce_tempo():
    global previous
    mean = 75
    sigma = 30
    upper = mean + 2 * sigma
    dist = stats.norm( mean, sigma )
    while True:
       delta = datetime.datetime.utcnow() - previous
       delta = delta.total_seconds()
       print delta
       t = dist.cdf( upper - delta ) * upper 
       if t < 20:
          t = 20
       out( 'tempo ' + str( int(t) ) )
       time.sleep( 2 )

t = Thread( target = reduce_tempo )
t.daemon = True
t.start()
