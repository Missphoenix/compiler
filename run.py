from CFGTree import *
from System import *

s = System()
quit = True
while quit:
	s.show()
	answer , correct = s.check()
	if correct == True:
		if answer == '5':
			quit = False
