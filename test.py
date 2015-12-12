from CFGTree import *
from System import *

s = System()
quit = True
while quit:
	s.show()
	answer , correct = s.Check()
	if correct == True:
		if answer == '3':
			quit = False