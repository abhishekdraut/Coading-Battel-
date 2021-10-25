def conversion(string):
    string = string.lower()                                   # to include capital letters
    for letter in string:
        if string.count(letter) > 1:                          # for characters having frequency more than 1
            string = string.replace(letter, ')')
        else:                                                 # for characters having frequency 1
            string = string.replace(letter, '(')
    return string

if __name__ == "__main__":                                                 
    string = input("Enter the string:- ")           #input from user  
    print(conversion(string))                                           # execution of function
    print("Program ended..................................")