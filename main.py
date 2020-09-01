# Author Hoang Bui hhb5051@psu.edu  
# Collaborator Adalia Chen asc209@psu.edu
# Collaborator Ved Walavalkar vtw5023@psu.edu   

temp = float(input("Enter temperature: "))
unit = (input("Enter unit in F/f or C/c: "))
if unit == 'C' or unit == 'c': 
  fah = (temp * 9/5) + 32
  print(f'{temp}° in Celsius is equivalent to {fah}° Fahrenheit.')
elif unit == 'F' or unit == 'f': 
  cel = (temp-32) / (9/5)
  print(f'{temp}° in Fahrenheit is equivalent to {cel}° Celsius.')
else: 
  print(f"Invalid unit({unit}).")