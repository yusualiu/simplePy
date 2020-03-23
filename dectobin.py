def dectobin():
  # accept input
  decimal = input('Please enter a number: ')
  decimal = int(decimal)
  binary = bin(decimal)[2:]  
  print(int(binary))
  
dectobin()