import password_gen

print('''\
                      .----.
      .---------. | == |
      |.-"""""-.| |----|
      ||       || | == |
      ||       || |----|
      |'-.....-'| |::::|
      `"")---(""` |___.|
     /:::::::::::\" _  "
    /:::=======:::\`\`\
    `"""""""""""""`  '-'
''')
print()
print()
print('''\
______                                   _   _____                           _             
| ___ \                                 | | |  __ \                         | |            
| |_/ /_ _ ___ _____      _____  _ __ __| | | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| | | (_| \__ \__ \\ V  V / (_) | | | (_| | | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   

''')

# Getting the total amount of characters required to fulfill password requirements
total_char_count = int(input("How many characters are required for your password?"))
print(f"{total_char_count} characters! Let's see what I can do for you!")
print()
print()

# Getting total amount of uppercase alpha characters required
upper_alpha_chars = int(input("How many UPPERCASE alpha characters are required?"))
print(f"{upper_alpha_chars} alpha characters? Roger that!")
print()
print()

# Getting total amount of numbers/numeric characters required
numeric_char_count = int(input("How many numeric characters are required?"))
print(f"{numeric_char_count} numeric characters. You got it!")
print()
print()

# Getting total amount of special characters required
special_char_count = int(input("How many special characters are required?"))
print(f"{special_char_count} special characters... On it!")
print()
print()


# Creating array to store all the generated characters inside.
pass_char_arr = []


# Generating however many alpha characters the user specified
for chars in range(upper_alpha_chars):
    pass_char_arr.append(password_gen.random_capitalized_alpha_char())


# Generating however many numeric characters the user specified
for chars in range(numeric_char_count):
    pass_char_arr.append(password_gen.random_numeric_char(0, 9))


# Generating however many special characters the user specified
for chars in range(special_char_count):
    pass_char_arr.append(password_gen.random_special_char())


# Calculating how many characters are left to fulfill the password length requirements.
leftover_chars = (total_char_count - len(pass_char_arr))

# Getting a random number so to make the password not NECESSARILY the required length.
total_char_count = password_gen.random_numeric_char(0, 5)
leftover_chars += total_char_count


# Generating lowercase alphas depending on how many leftover characters there are.
for chars in range(leftover_chars):
    pass_char_arr.append(password_gen.random_lower_alpha_char())


# Rearrange the order of all the characters in the password array.
pass_char_arr = password_gen.shuffle_password(pass_char_arr)
pass_char_arr = list(map(str, pass_char_arr))
password = ''.join(pass_char_arr)

print("loading... please wait for your new password to be generated!")
print()
print()
print("your new password is...")
print()
print()
print(password)








