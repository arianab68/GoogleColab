number = int(input("Enter a number: "))
if number%2 == 0:
  print(f"{number} in even") #f string
else:
  print("{0} is Odd".format(number))