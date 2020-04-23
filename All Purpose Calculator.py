import time

print("Welcome To The Calculator!!! ")

time.sleep(2)

print("1. Addition")
time.sleep(0.5)
print("2. Subtraction")
time.sleep(0.5)
print("3. Multiplication")
time.sleep(0.5)
print("4. Division")
time.sleep(0.5)
print("5. Square")
time.sleep(0.5)
print("6. Square root")
time.sleep(0.5)
print("7. Cube")
time.sleep(0.5)
print("8. Exit")

while True:
    print("...............")
    time.sleep(1)
    operation=input("Choose The Operation : ")
    time.sleep(1)
    
    if operation=="1":
        num1=input("Enter 1st No. : ")
        num2=input("Enter 2nd No. : ")
        print("Answer : " + str(int(num1)+int(num2)))
        
    elif operation=="2":
        num1=input("Enter 1st No. : ")
        num2=input("Enter 2nd No. : ")
        print("Answer : " + str(int(num1)-int(num2)))
    
    elif operation=="3":
        num1=input("Enter 1st No. : ")
        num2=input("Enter 2nd No. : ")
        print("Answer : " + str(int(num1)*int(num2)))
        
    elif operation=="4":
        num1=input("Enter 1st No. : ")
        num2=input("Enter 2nd No. : ")
        print("Answer : " + str(int(num1)/int(num2)))
        
    elif operation=="5":
        num1=input("Enter 1st No. : ")
        print("Answer : " + str(int(num1) ** 2)
        
    elif operation=="6":
        num1=input("Enter 1st No. : ")
        print("Answer : " + str(int(num1) ** (1/2))
        
    elif operation=="7":
        num1=input("Enter 1st No. : ")
        print("Answer : " + str(int(num1) ** 3)
    
    elif operation=="8":
        print("Thank You For Using!!! ")
        break
    else:
        print("Invalid Operation !!!")