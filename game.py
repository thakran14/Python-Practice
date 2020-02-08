# guess the dice number game
import random
import sys

if __name__ == "__main__":
 print("This is a dice number guessing program\n")

 while True :
  val = input("Press y to continue, n to exit\n")

  if val=='y':
   num = int(random.choice([1,2,3,4,5,6]))
   #print(num)
   #print(type(num))
   n = int(input("Guess the number on the dice\n"))
   #print(type(n))
   if num==n :
    print("You guessed it Right")			
   else :
    print("Wrong, Try again")
			

			
			
		
  elif val=='n':
   sys.exit(0)
            
	
			







