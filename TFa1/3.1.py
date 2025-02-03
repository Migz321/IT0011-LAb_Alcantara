first_name = input("Enter your first name: ")
Last_name = input("Enter your last name: ")
age = int(input("Enter your Age: "))

full_name = first_name + "" + Last_name
slice_name = full_name[0:3]
greeting_message = "Hello, {}! Welcome. You are {} years old.".format(slice_name, age)

print("Full_name:", full_name)
print("Sliece_name:", slice_name)
print("Greeting_message:", greeting_message)