
def traingle4(number):  #Driven function 
    spaces = number - 1 #Spaces
    for i in range(0, number):#Handle number of rows   
        for j in range(0, spaces):#Handle number spaces
            print(end=" ")     
        spaces = spaces - 1#decrementing k 
        for j in range(0, i+1): # Handle number of columns
            print("* ", end="")#  printing stars
        print("\r")         #end line after each row

    spaces = 0
    rows=number
    for i in range(rows-1, -1, -1):
        for j in range(spaces, 0, -1):
            print(end=" ")
        spaces = spaces + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print(" ")
            

    
    
if __name__ == "__main__":
    try:
        number = int(input("Enter the number of rows:- "))
        type = type(number)
        if number > 0:
            traingle4(number)
        elif number <= 0:
            print("Input should't be negative or zero. Please Enter positive number.")
    except ValueError:  # user define exeption handling;
        print("Input should not be string. Please Enter positive number.")
    finally:
        print("Program ended..................................")
