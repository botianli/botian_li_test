
def CompareTwoString(String1,String2) :
  try: #catch value error exception if cannot convert the String to float number
    number1=float(String1)
    number2=float(String2)
    # 3 cases
    if(number1>number2): #one number is greater
       print(f'{String1} is greater than {String2}')

    elif (number1==number2): #one number is smaller
        print(f'{String1} is equal to {String2}')
    else:                   #two numbers are equal
        print(f'{String1} is smaller than {String2}')

  except: #if catches exception, return this warning message
      print("Wrong input argument, String have to be number!")
