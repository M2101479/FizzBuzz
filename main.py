for x in range(1,51):
  if x % 3 == 0 and x % 5 ==0 :
    print("FizzBuzz")
  elif x % 5 == 0:
    print("Buzz")
  elif x % 3 == 0:
    print("Fizz")
  else:
    print(x)

number1=int(input("Enter a number"))
number2=int(input("Enter another number"))
number3=int(input("Enter another number"))
if number1 >=number2:
  if number1 >= number3:
    print(number1)
  else:
    print(number3)
elif number1 < number2:
  if number2 < number3:
    print(number3)
  else:
    print(number2)