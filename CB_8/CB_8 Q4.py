dictionary = {'a': 1, "e": 2, "i": 3, "o": 4, "u":5}
def encode(string):
    for letter in string:
        for key, value in dictionary.items():               # to iterate in dictionary
            if letter == key:
                string = string.replace(letter, str(value))   # replace key letter with its values
    print(string)

def decode(string):
    for letter in string:
        for key, value in dictionary.items():                  # to iterate in dictionary
            if letter == str(value):
                string = string.replace(letter, key)            # replace value letter with its key
    print(string)

if __name__ == "__main__":                                                 
    string = input("Enter the string:- ")           #input from user    
    print(encode(string))                                           # execution of function
    print("Program ended..................................")

if __name__ == "__main__":                                                 
    string = input("Enter the string:- ")           #input from user    
    print(decode(string))                                           # execution of function
    print("Program ended..................................")