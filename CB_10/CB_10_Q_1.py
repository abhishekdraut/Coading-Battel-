def devisor(input):
    halfvalue = input//2
    arraywithdevisor = []

    for i in range(2, halfvalue+1):
        if input % i == 0:

            arraywithdevisor.append(i)  #Adding values to array.

    return (arraywithdevisor)


if __name__ == "__main__":
    try:
        number = int(input("Enter the number :- "))  # input from user
        if number <= 0:                                         # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")

        # execution of function
        printTheArray = devisor(number)
        length = printTheArray.__len__()    #Finding out the array is empty or not is empty then number is prime  .

        if length == 0:
            print("The given Number is Prime number")

        else:

            print(
                "The Array with devisor, Without 1 and the number itself----------- \n", printTheArray)

    except ValueError:                                            # user define exeption handling; for strings input
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")
