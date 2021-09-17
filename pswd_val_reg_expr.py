#import regular expression 
import re
pswd=input("enter password here:")
pswd_len=len(pswd)
flag=1
while True:
    if pswd_len>=6 and pswd_len<=16:
        if not re.search("[a-z]",pswd):
            #print("make sure that ur pswd has atleast 1 letter between a-z and A-Z")
            flag=0
            break
        elif not re.search("[A-Z]",pswd):
           #print("make sure that ur pswd has atleast 1 letter between A-Z")
            flag=0
            break
        elif not re.search("[0-9]",pswd):
            #print("enter atleast 1 number between 0-9")
            flag=0
            break
        elif not re.search("[$#@]",pswd):
            #print("please enter atleast one character from [$#@]")
            flag=0
            break
        else:
            flag=1
            print("given password is valid")
            break
    else:
        print("please enter pswd atleat min 6 and max 16")
        break
if flag==0:
    print("Entered pswd is not valid")

