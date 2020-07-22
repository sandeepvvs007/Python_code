one=int(input("please enter first number"))
two=int(input("please enter second number"))
oper=input("please enter A for addition S for substraction M for multiplication D for division and X for exit").casefold()
while oper is not "e" :
    if oper =="a":
        print("sum is {}".format(one+two))
        break
    elif oper == "s":
        print("difference is {}".format(one-two))
        break
    elif oper == "m":
        print("product is {}".format(one*two))
        break
    elif oper == "d":
        print("division result is {}".format(one/two))
        break
    else:
        print("please enter a valid input")
        break

