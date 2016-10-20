'''
Program that prints out the numbers 1 to 100 (inclusive). 
If the number is divisible by 3, print Crackle instead of the number. 
If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop.
'''


def divisible_number(): 
  
  for i in range(1,101): 
    if (i % 3 == 0 and i % 5 == 0):
      print "CracklePop"
    elif (i % 3 == 0):
      print "Crackle"
    elif (i % 5 == 0):
      print "Pop"
    else: 
      print(i) 

if __name__ == "__main__":
  divisible_number()