import math

chord = {
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
	if x < 10:
		return str( x )
	return '10'

def sonify( data ):
# delta, mean mood, this mood, mean weight, this weight, voices
   print 'chordtype ' + chord[ round( data[1] ) ]
   print 'voices ' + _voices( data[5] )
   print 'rythmdensity ' + _density( data[3] )

## initial
print 'sound on'
print 'globalvolume 75'