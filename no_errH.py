#prompt
msg = "Please enter a integer to check if it is a leap year: "
print(msg)
yes = "is a leap year!"
no = "is not a leap year!"

#store input
input_data = input()
input_data = int(input_data)


#looping for verification
if (input_data % 4 == 0):
    if(input_data % 100 == 0):
        if(input_data % 400 == 0):
            print(input_data,yes)
        else:
            print(input_data,no)
    else:
        print(input_data,yes)
else:
    print(input_data,no)