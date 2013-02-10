chord = {
	0 : 'major',
	1 : 'major7',
	2 : 'majormaj7',
	3 : 'major6',
	-1: 'minor',
	-2: 'minor7',
	-3: 'minormaj7',
}

import math

def sonify( data ):
# delta, mean mood, this mood, mean weight, this weight
   print 'chordtype ' + chord[ round( data[1] ) ]

## initial
print 'sound on'
print 'globalvolume 75'