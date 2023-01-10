"""
4. Palindrome
You are given a string str. You can convert str to a palindrome by adding characters in front of it. Return the shortest palindrome you can find by performing this transformation.
Restrictions:
You must not use any libraries for this exercise.

"""

def check_Polindrom():
    string = str(input())
    front_letters = ""
    temp = string

    while string != string[::-1]:
        front_letters += string[-1]
        string = string[:len(string) - 1]

    print(front_letters + temp)

    
check_Polindrom()