import math
import sys

file = open('data', 'a' )

def out( data ):
	if isinstance(data, list ):
		data = '\n'.join(data)
	file.write( data + '\n' )
	file.flush()
	print data

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

delta = 0

harmonity = {
-3 : '1',
-2 : '1',
-1 : '1',
0 : '5',
1 : '6',
2 : '9',
3 : '10'
}

def sonify( data ):
   global delta
# delta, mean mood, this mood, mean weight, this weight, voices
   out( [
   		'scaletype ' + _chord[ round( data[1] ) ],
		'harmony ' + harmonity[ round( data[1] ) ],
   		'voices ' + _voices( data[5] ),
   		'rythmdensity ' + _density( data[3] )
   	] )
   delta = data[0]

## initial
out( [ 'sound on', 'drums on', 'tempo 100' ] )


## thead for reducing tempo
import time
from threading import Thread

def reduce_tempo():
    global delta
    while True:
       d = int(time.time() - delta - 120*60) ## server time off by 2h
       t = round( 240 - d ) + 10
       if t < 10:
          t = 10
       out( 'tempo ' + str( t ) )
       time.sleep( 2 )

t = Thread( target = reduce_tempo )
t.daemon = True
t.start()
