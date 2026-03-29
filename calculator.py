def is_num(str):
    try:
        float(str)
        return True
    except ValueError:
        return False



print("Hello, I am a calculator!  Type what mathematical equation you would like accomplished!")
while True:
    num_one = input("Please type the first number:")
    if is_num(num_one): 
        break
    else:
        print("Please enter a valid number")

while True:
    num_two = input("Please type the second number:")
    if is_num(num_two):
        break
    else:
        print("Please enter a valid number")

while True:
    operator = input("Please type what calculation you would like performed, + - * /:")
    if operator.lower() == "+" or operator.lower() == "add":
        print(float(num_one) + float(num_two))
        break
    elif operator.lower() == "-" or operator.lower() == "subtract" :
        print(float(num_one) - float(num_two))
        break
    elif operator.lower() == "*" or operator.lower() == "multiply":
        print(float(num_one) * float(num_two))
        break
    elif operator.lower() == "/" or operator.lower() == "divide":
        print(float(num_one) / float(num_two))
        break
    else:
        print("Please enter a valid operator")
