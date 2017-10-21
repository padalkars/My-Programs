'''
Say you want to find a phone number in a string. You know the pattern:
three numbers, a hyphen, three numbers, a hyphen, and four numbers.
Here’s an example: 415-555-4242.
'''

def isPhoneNumber(ph):

    if(len(ph)!=12):
        return False
    
    for i in range(len(ph)):
        
        if(ph[3]!='-'):
            return False
        if(ph[7]!='-'):
            return False
        if(ph[i] not in range(10)):
            return False
        
    
    return True

x = input()

if(isPhoneNumber(x)):
    print("A valid phone number")
else:
    print("Please enter a valid phone number")

