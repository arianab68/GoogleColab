def sum_int(num):
  sum = 0 #Starting at 0
  
  if num != int(num): #Checking If num is not an integer
    print('Wrong input...BYE!')
    print('0')

  else:
    for i in range (num + 1): #For every input of i i in the range of the value of num+1
      sum += i #calculate the sum for every input of i 
  return (f'The sum is {total}')

 