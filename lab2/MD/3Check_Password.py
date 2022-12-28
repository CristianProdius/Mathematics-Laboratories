"""
3. Check password
We all use many passwords every day but is every password we use hard enough to crack. Your password is considered strong if it follows this rules:
-It has at least 8 characters and at most 20 characters.
-It has a minimum of 1 lower case letter [a-z] and a minimum of 1 upper case letter [A-Z] and a minimum of 1 numeric character [0-9] and a minimum of 1 special character: ~`!@#$%^&*()-_+={}[]|\;:"<>,./?
-It does not contain three repeating characters in a row (i.e.,“abbbcc-0”is weak, but  is “ abcbbcc-0”strong).
Given a string password, return the minimum number of steps required to make the password strong. If the password is already strong, return the message “good”.
In one step, you can: 
-Insert one character 
-Delete one character 
-Replace one character
Restrictions:
You must not use any libraries for this exercise.

"""
def max_repeted_charachters(password):
    max_repeted_charachters = 0
    for i in range(len(password)):
        current_count = 1
        for j in range(i + 1, len(password)):
            if password[i] == password[j]:
                current_count += 1
            else:
                break
        if current_count > max_repeted_charachters:
            max_repeted_charachters = current_count 
    return max_repeted_charachters  

def lower_letter(password):
    frequency_lower_letter = 0
    for i in range(len(password)):
        if 97<=ord(password[i])<=122:
            frequency_lower_letter += 1
    return frequency_lower_letter

def upper_letter(password):
    frequency_upper_letter = 0
    for i in range(len(password)):
        if 65<=ord(password[i])<=90:
            frequency_upper_letter += 1
    return frequency_upper_letter

def numbers(password):
    frequency_numbers = 0
    for i in range(len(password)):
        if 48<=ord(password[i])<=57:
            frequency_numbers += 1  
    return frequency_numbers  

def special_charachters(password):
    special_charachters = 0
    for i in range(len(password)):
        if 32<=ord(password[i])<=47 or 58<=ord(password[i])<=64 or 91<=ord(password[i])<=96 or 123<=ord(password[i])<=126:
            special_charachters += 1                     
    return special_charachters


def check_password_strong(password):
    #Pasword Information
    max_frequency_consecutive_charachters = max_repeted_charachters(password)
    frequency_lower_leters = lower_letter(password)
    frequency_upper_leters = upper_letter(password)
    frequency_numbers = numbers(password)
    frequency_special_charachters = special_charachters(password)

    if 8<=len(password)<=20 and  max_frequency_consecutive_charachters<3 and frequency_lower_leters>0 and frequency_upper_leters>0 and frequency_numbers>0 and frequency_special_charachters>0:
        return True
    else:
        return False
                       

def minimum_steps_to_make_pass_strong(password):
    #Pasword Information
    max_frequency_consecutive_charachters = max_repeted_charachters(password)
    frequency_lower_leters = lower_letter(password)
    frequency_upper_leters = upper_letter(password)
    frequency_numbers = numbers(password)
    frequency_special_charachters = special_charachters(password)

    steps = 0
    if frequency_lower_leters == 0:
        steps += 1
    if frequency_upper_leters == 0:
        steps += 1
    if frequency_numbers == 0:
        steps += 1
    if frequency_special_charachters == 0:
        steps += 1

    if steps + len(password) < 8:
        steps = 8 - len(password)
    if steps + len(password) > 20:
        length_password = len(password)
        steps_to_short_password = 0
        while length_password > 20:
            length_password -= 1            
            steps_to_short_password += 1
        steps = steps + steps_to_short_password
    if steps + max_frequency_consecutive_charachters > 8:
        while max_frequency_consecutive_charachters > 2:
            steps += 1
            max_frequency_consecutive_charachters -= 1

    return steps



    
#input Section
password = input("Enter the passwrod: ")

#Decision Section
if check_password_strong(password):
    print("good")
else:
    print("The minimum steps to make the password strong is: " + str(minimum_steps_to_make_pass_strong(password)))