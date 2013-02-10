import math

out = open('data', 'a' )

_chord = {
	0 : 'major',
	1 : 'major7',
	2 : 'majormaj7',
	3 : 'major6',
	-1: 'minor',
	-2: 'minor7',
	-3: 'minormaj7',
}

def _voices( voices ):
	if voices < 3:
		return str( voices )
	if voices < 5:
		return '4'
	if voices < 10:
		return '5'
	return '6'

def _density( mean ):
	## TODO: check this from empirical logs!
	x = int( mean / 20 ) + 1
	return str( x ) if x < 10 else '10'

def _tempo( delta ):
	x = 150 * delta / 60000
	tempo = 250 - x
	return str( tempo ) if tempo > 5 else '5'

def sonify( data ):
# delta, mean mood, this mood, mean weight, this weight, voices
   out.write( 'chordtype ' + _chord[ round( data[1] ) ] + '\n' )
   out.write( 'voices ' + _voices( data[5] ) + '\n' )
   out.write( 'rythmdensity ' + _density( data[3] ) + '\n' )
   out.write( 'tempo ' + _tempo( data[0] ) + '\n' )
   out.flush()

## initial
out.write( 'sound on \n' )
out.write( 'globalvolume 75 \n' )
out.write( 'tempo 100 \n' )
out.flush()
