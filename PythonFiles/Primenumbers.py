for num in range (2,101): # for the numbers within the range 
  # num % i produces the remainder when num is divided by i.
  # The all method returns True when all elements are true.
  if all (num%i != 0 for i in range (2,num)): #if num % i is not equal to 0, then for i in the range (2,num) print num
    print(num) #prints the num