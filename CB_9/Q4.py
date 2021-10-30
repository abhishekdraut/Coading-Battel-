def sumOfLetters(letters):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    sum = 0
    for letter in letters:
        sum += (alphabets.index(letter)+1)                    # find the value of letter
    count = sum % 26
    return alphabets[count-1]                                 # return the letter of value

if __name__ == "__main__":
    array = []
    string = input("Enter comma&space(', ') separated names :- ")           #input from user 
    error = False
    if string:
        array = string.split(', ')
        for name in array:
            if ',' in name or name.isdigit():
                print('please enter names like a, b, c, d, e')
                error = True
                break
    if not error:
        print(sumOfLetters(array))                         # execution of function
    print("Program ended..................................")