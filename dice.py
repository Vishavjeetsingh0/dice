import code


while True:
    user_input=int(input("enter the number of dice"))
    if user_input == 0:
        break
    code.get_dice(user_input)
