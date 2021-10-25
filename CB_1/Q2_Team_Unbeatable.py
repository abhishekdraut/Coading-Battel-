#2
def traingle2(n):
    for i in range (n):
        print('* '*(n-i))

if __name__ == "__main__":
    try:
        number = int(input("Enter the number of rows:- "))
        if number > 0:
            traingle2(number)
        elif number <= 0:
            print("Input should't be negative or zero. Please Enter positive number.")
    except ValueError:  # user define exeption handling;
        print("Input should not be string. Please Enter positive number.")
    finally:
        print("Program ended..................................")
