def func(n):
    for i in range(1, n+1): #outer loop to handle number of rows
        for j in range(i, n+1): #inner loop to handle number spaces
            if(i == 1 or j == i or j == n): #for printing star on row and column
                print(j, end = " ") #printing numbers
            else:
                 print(" ", end = " ") #ending line after each row
        print()

if __name__ == "__main__":                                                 
    try:
        number = int(input("Enter the number of rows:- "))            #input from user             
        if number <= 0:                                               # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")
        
        func(number)                                         # execution of function
    except ValueError:                                            # user define exeption handling; for strings input   
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")



