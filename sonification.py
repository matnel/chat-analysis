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
	if voices <= 5:
		return str( voices )
	if voices < 10:
		return '6'
	if voices < 15:
		return '7'
	return '8'

def _density( mean ):
	## TODO: test more!
	## TODO: check this from empirical logs!
	x = int( mean / 10 ) + 2
	return str( x ) if x < 16 else '16'

tempo = 0

def _tempo( delta ):
	global tempo
	x = delta * 1.5
	if int( 150 - x ) > tempo:
        	tempo = int( 150 - x )
	return str( tempo ) if tempo > 5 else '5'

def sonify( data ):
# delta, mean mood, this mood, mean weight, this weight, voices
   out( [
   		'scaletype ' + _chord[ round( data[1] ) ],
		'harmonity ' + str( int( 5 + data[1] ) ),
   		'voices ' + _voices( data[5] ),
   		'fraselenght ' + _density( data[3] ),
   		'tempo ' + _tempo( data[0] )
   	] )

## initial
out( [ 'sound on', 'drums on', 'tempo 100' ] )


## thead for reducing tempo
import time
from threading import Thread

def reduce_tempo():
    global tempo
    while True:
       tempo = tempo - 5
       if tempo < 5:
           tempo = 5
       out( 'tempo ' + str( tempo ) )
       time.sleep( 5 )

t = Thread( target = reduce_tempo )
t.daemon = True
t.start()
