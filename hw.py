try:
    age = int(input("Enter your age: "))
    print("your age is", age)
    if age%2==0:
        print("your age is even")
    else:
        print("your age is odd")
except:
    print("Invalid!!")