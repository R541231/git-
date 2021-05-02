# # print("Enter the number which you want to calculate.")
# # # print("Enter the second number")
# # a=input()
# # # b=input()
# # if a==2+2:
# #     print("11")
# # # elif 


# print("type what you wanted to calculate\ntype'+'for addition,\n '-'for subtraction \n'*'for multiplication \n'/' for division")
# p=input("enter your first number")
# p=int(p)
# q=input("enter your second number")
# q=int(q)
# h=input("choose operator for ex:(+,-,*,/):")


# if (h=="+"):
#     if (p==56 and q==67 or p==67 and q==56):
#         print ("64646")
#     else:
#         print (p+q)
# if (h=="-"):
    
# if (p==34 and q==98 or p==98 and q==34):
#     print ("646655")
#     else:
#         print (p-q)
# if(h=="*"):

#     if (p==45 and q==64 or p==64 and q==45):
#         print ("656")
#     else:
#         print (p*q)
# if(h=="/"):
#     if (p==49 and q==7 or p==7 and q==49):
#         print("23")
#     else:
#         print (p/q)

import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
  
    print "Rock, Paper, Scissors - Shoot!"
    userChoice = raw_input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print "Please choose a letter:"
        print "[R]ock, [S]cissors or [P]aper."
        continue
    // Echo the user's choice
    print "You chose: " + userChoice
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print "I chose: " + opponenetChoice
    if opponenetChoice == str.upper(userChoice):
        print "Tie! "
    #if opponenetChoice == str("R") and str.upper(userChoice) == "P"
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':      
        print "Scissors beats rock, I win! "
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':      
        print "Scissors beats paper! I win! "
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':      
        print "Paper beat rock, I win! "
        continue
    else:       
        print "You win!"