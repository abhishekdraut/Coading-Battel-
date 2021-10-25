def hashAsBackspace(string):
    while '#' in string:                                        # check if # is in string 
        for index in range(len(string)):
            if string[index] == '#' and index != 0:             # find position of #
                old = string[index-1]+string[index]             # find what to replace # and its previous letter
                string = string.replace(old, "", 1)             # delete both letters
                break
            if string[0] == '#':
                string = string.replace('#', "", 1)             # for more # than letters
    return string

if __name__ == "__main__":                                                 
    string = input("Enter the string:- ")                                 #input from user    
    print(hashAsBackspace(string))                                           # execution of function
    print("Program ended..................................")