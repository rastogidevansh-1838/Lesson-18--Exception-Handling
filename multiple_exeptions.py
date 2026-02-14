try:
    num1, num2 = eval(input("enter two numbers, separated by a comma: "))
    result = num1 / num2
    print("result is", result)
except ZeroDivisionError:
    print("Division by 0 is errror!!")
except SyntaxError:
    print("Comma is missing, Enter numbers separarted by comma like this: 1, 2")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")