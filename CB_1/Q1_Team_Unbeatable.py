#1
def print_rectangle(n, m) :
     
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            if (i == 1 or i == n or
                j == 1 or j == m) :
                print("* ", end="")           
            else :
                print("  ", end="")           
        print()
 
if __name__ == "__main__":
    try:
        rows = int(input("enter row:"))
        columns = int(input("enter col:"))
        if rows > 0 and columns>0:
            print_rectangle(rows, columns)
        elif rows <= 0 or columns <= 0:
            print("Input should't be negative or zero. Please Enter positive number.")
    except ValueError:  # user define exeption handling;
        print("Input should not be string. Please Enter positive number.")
    finally:
        print("Program ended..................................")
