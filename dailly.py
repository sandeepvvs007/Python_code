one=int(input("please enter first number"))
two=int(input("please enter second number"))
oper=input("please enter A for addition S for substraction M for multiplication D for division and X for exit").casefold()
while oper != "e" :
    if oper =="a":
        print("sum is {}".format(one+two))
    elif oper == "s":
        print("difference is {}".format(one-two))
    elif oper == "m":
        print("product is {}".format(one*two))
    elif oper == "d":
        print("division result is {}".format(one/two))
    else:
        print("please enter a valid input")
    one=int(input("please enter first number"))
    two=int(input("please enter second number"))
    oper=input("please enter A for addition S for substraction M for multiplication D for division and X for exit").casefold()
    
    
    
    n=int(input("enter the value of n"))
for i in range(n):
    print("*"*i)
for i in range(n,0,-1):
    print("*"*i)
