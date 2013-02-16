import math

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
	x = int( mean / 20 ) + 1
	return str( x ) if x < 10 else '10'

def _tempo( delta ):
	x = 150 * delta / 60000
	tempo = 250 - x
	return str( tempo ) if tempo > 5 else '5'

def sonify( data ):
# delta, mean mood, this mood, mean weight, this weight, voices
   out( [
   		'scaletype ' + _chord[ round( data[1] ) ],
		'harmonity ' + str( 5 + round( data[1] ) ),
   		'voices ' + _voices( data[5] ),
   		'rythmdensity ' + _density( data[3] ),
   		'tempo ' + _tempo( data[0] )
   	] )

## initial
out( [ 'sound on', 'drums on', 'globalvolume 75' , 'tempo 100' ] )
