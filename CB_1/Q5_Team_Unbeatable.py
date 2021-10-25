#5
def invertedtraingle(rows):
    k = 0
    for i in range(rows-1, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print(" ")
        
if __name__ == "__main__":
    try:
        number = int(input("Enter the number of rows:- "))
        type = type(number)
        if number > 0:
            invertedtraingle(number)
        elif number <= 0:
            print("Input should't be negative or zero. Please Enter positive number.")
    except ValueError:  # user define exeption handling;
        print("Input should not be string. Please Enter positive number.")
    finally:
        print("Program ended..................................")