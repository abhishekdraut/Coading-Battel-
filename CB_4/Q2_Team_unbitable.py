def empty_diamond(row): #define function
    for i in range(1, row+1): #upper triangle shape
        for j in range(1,row-i+1): #print space
            print(" ", end="")
        for j in range(1, 2*i): #print *
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for i in range(row-1,0, -1): #lower triangle shape
        for j in range(1,row-i+1): #print space
            print(" ", end="")
        for j in range(1, 2*i): #print star
            if j==1 or j==2*i-1:
               print("*", end="")
            else:
                print(" ", end="")
        print()
if __name__ == "__main__":                                                 
    try:
        number = int(input("Enter the number of rows:- "))            #input from user             
        if number <= 0:                                         # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")
        
        empty_diamond(number)                                           # execution of function
    except ValueError:                                            # user define exeption handling; for strings input   
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")