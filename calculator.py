#Send error when input is not a number
#Allow to type number out

def is_num(str):
    try:
        float(str)
        return True
    except ValueError:
        return False



print("Hello, I am a calculator!  Type what mathematical equation you would like accomplished!")
num_one = input("Please type the first number:")
if is_num(num_one): 
    pass
else:
    print("Please enter a valid number")


num_two = input("Please type the second number:")
operator = input("Please type what calculation you would like performed, + - * /:")

if is_num(num_one): 
    pass
else:
    print("Please enter a valid number")

if operator.lower() == "+" or operator.lower() == "add":
    print(float(num_one) + float(num_two))
elif operator.lower() == "-" or operator.lower() == "subtract" :
    print(float(num_one) - float(num_two))
elif operator.lower() == "*" or operator.lower() == "multiply":
    print(float(num_one) * float(num_two))
elif operator.lower() == "/" or operator.lower() == "divide":
    print(float(num_one) / float(num_two))

