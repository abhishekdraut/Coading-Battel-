#6
def print_tringle(number):
    even_space = 2  # even Spaces like col 2,col 4,col 6
    for row in range(1, number+1):
        for col in range(1, 2*number):
            if row+col == number+1 or col-row == number-1:  # condition for printing stars except last row;
                print("*", end="")
            elif row == number and col != even_space:  # condition for printing stars at last row;
                print("*", end="")
                even_space = even_space+2
            else:
                print(end=" ")  # condition for printing space
        print(" ")

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