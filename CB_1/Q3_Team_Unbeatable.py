#3
def halfpyramid(n):  #Function for printing triangle
        for i in range(n):   #outer loop to handle number of rows
            for j in range(n):          #inner loop to handle number spaces
                if j==0 or i==0  or i + j==(n-1): #for printing star on row and column
                    print("*",end="")       #printing stars
                else:
                 print(" ",end="")  #ending line after each row
            print()

if __name__ == "__main__":
    try:
        number = int(input("Enter the number of rows:- "))
        type = type(number)
        if number > 0:
            halfpyramid(number)
        elif number <= 0:
            print("Input should't be negative or zero. Please Enter positive number.")
    except ValueError:  # user define exeption handling;
        print("Input should not be string. Please Enter positive number.")
    finally:
        print("Program ended..................................")
