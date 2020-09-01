temp = float(input("Enter temperature: "))
unit = (input("Enter unit in F/f or C/c: "))
if unit == 'C' or unit == 'c': 
  fah = (temp * 9/5) + 32
  print(f'{temp}° in Fahrenheit is equilvalent to {fah}° Fahrenheit')

elif unit == 'F' or unit == 'f': 
  cel = (temp-32) / (9/5)
  print(f'{temp}° in Celsius is equilvalent to {cel}° Celsius')

else: 
  print("invalid unit(bad)")