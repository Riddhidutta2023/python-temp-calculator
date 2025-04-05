# This calculator converts a given temperature to either farenheight or celsius


output = None
print("Welcome to the temperature converter")
print("====================================")
print("Write F for farenheight and C for celcius\n")

#converts the answer and provides input validation
answer = input("If you want Celsius to Farenheight conversion -write F or write C for farenheight to Celsius\n")
answer = answer.upper()
if answer=='F' and type == 'str':
    print("you chose to convert to Farenheight\n")
elif answer=='C' and type == 'str':
    print("You chose to convert to Celsious\n")
else:
    print('Your input was invalid')
    
#prints out required temperature using celsius to farenheight formula
    
temp = int(input("Enter the temperature you want to convert\n"))

if answer == 'F':
    output= (temp * 1.8) + 32
if answer == 'C':
    output = (temp - 32)/1.8
    

print(f"\nYour answer is {output} degree.")