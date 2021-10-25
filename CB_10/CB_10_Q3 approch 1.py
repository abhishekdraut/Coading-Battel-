
def check(inputstring):
    array1 = []
    array2 = []
    arrayWithBrackets = []
    string = inputstring
    length = string.__len__()  # getting the length of string.

    # making two copies of input string in the form of array .
    for z in range(0, length):
        array1.append(string[z])
        array2.append(string[z])

    indicator = 0  # act as a flag to inssure duplicate elements.

    # This loop checks each element of the first array to whole second array.
    for i in range(0, length):
        for j in range(0, length):
            if array1[i] == array2[j]:
                indicator += 1  # if finds duplicate indicator increments.

        # If the number is greater than 2 then the array must contains duplicates.
        if indicator >= 2:
            arrayWithBrackets.append(")")
        else:
            arrayWithBrackets.append("(")

        indicator = 0  # decrementing the value back to 0 for next iteration.

    for each in arrayWithBrackets:  # printing out the array in the string format.
        print(each, end="")
    print(end="\n")


if __name__ == "__main__":
    try:
        string = input("Enter the string:- ")  # input from user.
        string = string.lower()

        # execution of function
        check(string)

    finally:                                                          # to run after every execution
        print("Program ended..................................")
