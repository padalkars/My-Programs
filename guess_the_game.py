import random

class entry():
    d = []
    f = 0
    def validate(self):
        if(self.f==0):
            print("I am thinking of a number between")
        
        self.d = input().split(' ')
        a = int(self.d[0])
        b = int(self.d[1])

        if(a>b):
            print("Please re-enter the numbers. First number must be smaller than the second one.")
            del self.d
            self.f = 1
            self.validate()
        else:
            return self.d

    def guess(self):
        l = []
        count = 0
        l = self.validate()
         
        print("Take a guess.")
        x = int(input())
         
        actual_no = (random.randint(int(l[0]),int(l[1])))

        while(x):
            
            if(x<actual_no):
                print("Your Guess is too low")
                print("Take a guess")
                
                count += 1
                 
            elif(x>actual_no):
                print("Your Guess is too high")
                print("Take a guess")
                
                count += 1
                 
            else:
                count += 1
                print("You guessed the number right in "+ str(count)+" attempts")
                
                break
            x = int(input())     

e = entry()
l = []
l = e.guess()

