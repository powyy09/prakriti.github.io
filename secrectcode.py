import random as random
import string as str

string = input("Enter a string")

# encode the provided string
length= len(string)
print ( "length of given string is ",length)

if length < 3:
    # print (string[1]+string[0])
    print ("encoded string= ",string[::-1])
else:
   choice = str.ascii_letters
   firstCharacter = string[0]
   remainingString  = string[1::]
   popedString =  remainingString + firstCharacter
   encodedString = "".join(random.sample(choice,3))+popedString+"".join(random.sample(choice,3))
   print ("encoded string=",encodedString)


# decode the string
LengthOfEncoded = len(encodedString)
if LengthOfEncoded < 3:
    print("decoded string=", encodedString[::-1])    

else:
    mainString= encodedString[3:-3]
    actualmainString= encodedString[3:-4]
    lastOfMainSritng = mainString[-1]
    decodedString= lastOfMainSritng + actualmainString
    print ("decoded stirng=", decodedString)

