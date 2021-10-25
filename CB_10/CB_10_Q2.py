# Important Note if you want to use dynamic approch ,It is also implemented in the Program just uncomment it and comment out static part.

def autocomplete(string, inputArray):
    autosearch = []
    lengthOfString = string.__len__()  # finding the length of the string.
    lengthOfArray = inputArray.__len__()  # finding the length of the array.
    for i in range(0, lengthOfArray):
        eachSearch = inputArray[i]
        if string == eachSearch[:lengthOfString]:
            autosearch.append(eachSearch)

    key = 1
    print("following are the searches from Array/DB")
    for j in autosearch:
        print(key, end=" ")
        print(j)
        key += 1


if __name__ == "__main__":
    try:
        # input from user
        inputArray = []
        string = input(
            "Enter the string you want to search in database Array:---")

        # Static Array.
        inputArray = ['airplane', 'airport',
                      'apple', 'ball', 'airforce']

        # Alternative but you have to enter the array elements ,Dynamic Array using loop;
        # for i in range (1,6):
        #     searches=input("Enter the {} search element in array:--".format(i))
        #     inputArray.append(searches)

        # execution of function
        autocomplete(string, inputArray)  # passing the input and array.
    except ValueError:                                            # user define exeption handling; for strings input
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")
