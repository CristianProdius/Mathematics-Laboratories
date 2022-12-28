def check_Polindrom():
    string = str(input())
    front_letters = ""
    temp = string

    while string != string[::-1]:
        front_letters += string[-1]
        string = string[:len(string) - 1]

    print(front_letters + temp)

    
check_Polindrom()