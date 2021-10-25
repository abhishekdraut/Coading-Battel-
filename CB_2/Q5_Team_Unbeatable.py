def empty_pyramid(n):
    
    for row in range (1,n+1):                      #outer loop to handle number of rows
        print((n-row)*"  ",end="")                 # to print spaces first
        for col in range(1,n+1):                   #inner loop to handle number of columns
            if(col==1)or (row==n) or (row==col):  #for printing numbers on row and column
                print(col,end="   ")              #printing numbers and spaces
            else:
                print("    ",end="")              #spaces and ending line after each row
        print()                                  # to come on new line

if __name__ == "__main__":                                                 
    try:
        number = int(input("Enter the number of rows:- "))            #input from user             
        if number <= 0:                                         # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")
        
        empty_pyramid(number)                                           # execution of function
    except ValueError:                                            # user define exeption handling; for strings input   
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")