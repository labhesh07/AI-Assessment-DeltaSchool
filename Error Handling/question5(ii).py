try:
    answer=input("what should i divide 10 by?")
    num=int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("you can't divide by zero")
except ValueError as e:
    print("you don't give me a valid number")
    print(e)
finally:
    print("this code always run")
