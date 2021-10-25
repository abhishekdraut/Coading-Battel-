def print_tringle(input):          # working driven function;
    for i in range(1, input+1):      # loop for printing the tringle - to access rows
        for j in range(1, i+1):       # to access columns
            print(j, end=' ')        # to print numbers and spaces
        print(" ")                # to come on next line

if __name__ == "__main__":                                                 
    try:
        number = int(input("Enter the number of rows:- "))            #input from user             
        if number <= 0:                                         # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")
        
        print_tringle(number)                                           # execution of function
    except ValueError:                                            # user define exeption handling; for strings input   
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")