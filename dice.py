# dice simulator
import random
import sys

if __name__ == "__main__":
	while True :
		print("This is a dice simulator program")
		val = input("Press y to continue, n to exit")
	
		if val=='y':
			print(random.choice([1,2,3,4,5,6]))
		
		elif val=='n':
			sys.exit(0)
            
	







