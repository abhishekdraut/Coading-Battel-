#Test Cases
#input==19
#Input=7
#input=11
#input=31


def print_tringle(number):
    input = number
    n = input-1
    space = n
    in_tringle_space = 1


    for rows in range(1, n+1):
        for spaces in range(1, (2*space)+1):
            print(" ", end="")
        space -= 1
        print(end="")
    # spaces loop ends here;

    # loop for first-Star start here;
        if rows == 1:
            print("*")
            print(end="\n")
        else:
            print("*"+(2*in_tringle_space-1)*" ", end="")

            print("*"+(2*in_tringle_space-1)*" ", end="")

            print("*"+(2*in_tringle_space-1)*" ")
            print(end="\n")

            in_tringle_space += 1
    #printing the base line for both tringle
    print("* "*(2*input-1))
    print(end="\n")
    
    #using the spaces of up tringle
    space += 2
    in_tringle_space -= 1

    #loop for bottom star
    for row2 in range(1, n+1):
        print(" "*(space),end="")#printing the spaces
        space += 2

     #printing the lower tringle   
        if row2==n:
            print("*")
            print(end="\n")
        else:
            print("*"+(2*in_tringle_space-1)*" ", end="")

            print("*"+(2*in_tringle_space-1)*" ", end="")

            print("*"+(2*in_tringle_space-1)*" ")
            print(end="\n")
            in_tringle_space -= 1

if __name__ == "__main__":
    try:
        number = int(input("Enter the number of rows:- "))
        type = type(number)
        if number > 0:
            print_tringle(number)
        elif number <= 0:
            print("Input should't be negative or zero. Please Enter positive number.")
    except ValueError:  # user define exeption handling;
        print("Input should not be string. Please Enter positive number.")
    finally:
        print("Program ended..................................")
