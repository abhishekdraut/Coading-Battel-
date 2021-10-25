def pattern(n):
    for i in range(n, 0, -1):           #to handle rows: reverse range as pattern is reverse
        for j in range(1, i + 1):          #to handle columns
            print(j, end=" ")            #to print number and space
        print("")                     #to come on next line
 
if __name__ == "__main__":                                                 
    try:
        number = int(input("Enter the number of rows:- "))            #input from user             
        if number <= 0:                                         # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")
        
        pattern(number)                                           # execution of function
    except ValueError:                                            # user define exeption handling; for strings input   
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")
