def camelBreak(string):
    for letter in string:
        if letter.isupper():                                # check for capital letter
            string = string.replace(letter, ' '+letter)     # replace capital letter with a space
    return string


if __name__ == "__main__":                                                 
    string = input("Enter the string:- ")           #input from user    
    print(camelBreak(string))                                           # execution of function
    print("Program ended..................................")