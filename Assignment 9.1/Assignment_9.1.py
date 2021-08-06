import os

#Prompts for file path
print("Please enter a file path using forward slashes (/) where you would like your file.\n")
file_path = input("File path: ")

#Prompts for file name
print("\nPlease enter a file name for the file.\n")
file_name = input("File name: ")

#Prompts for user information
print("What is your name, address, and phone number?\n")

name = input("Name: ")
address = input("Address: ")
phone = input("Phone number: ")

file_path_exists = False

#Checks to see if a file path exists
#If not, loops until valid file path is given
while file_path_exists == False:
    try:
        with open(f'{file_path}/{file_name}.txt', 'w') as file_object:
            file_object.write(f"{name},{address},{phone}")
            file_path_exists = True

    except:
        print("File path does not exist, please enter a valid file path.")
        file_path = input("File path: ")

#Reads contents from file by splitting line based on comma delimiter
print("\nTo validate, here is your information.\n")

with open(f'{file_path}/{file_name}.txt') as file_object:
    string_list = file_object.read()
    string_list = string_list.split(',')
    print(f"Name: {string_list[0]}")
    print(f"Address: {string_list[1]}")
    print(f"Phone number: {string_list[2]}")




