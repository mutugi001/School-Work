#collins Mutugi Wachira
#SCT 211-0051/2022

name = input("enter name: ")
print("hello " + name)

num1 = input("enter num1: ")
num1 = int(num1)
opr = input("enter operator: ")
num2 = input("enter num2: ")
num2 = int(num2)

if opr == "+":
    sum = num1 + num2
    print(sum)


elif opr == "-":
    diff = num1 - num2
    print(diff)

elif opr == "*":
    mlt = num1 * num2
    print(mlt)
    
elif opr == "%":
    mod = num1 % num2
    print(mod)

elif opr == "/":
    if num2 == "0":
        print("division by zero!!")
    else:
        div = num1 / num2
        print(div)
        
else:
    print("error!!")
    
