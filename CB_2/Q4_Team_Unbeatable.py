def design(n):
    x= 0
    k = n - 1
    for row in range(1, n + 1) : #outer loop to handle number of rows
        x = row
        for col in range(1, k + 1) : #for loop to print spaces in row
            print(" ", end=" ")
        k = k - 1                    #display corresponding value
            
        for i in range(1, row + 1) :  #for loop to print gaps numbers incrementation in row
            print(x, end=" ")
            x = x + 1
        
        x = x - 2
        for i in range(1, row) : #to print another side right angle in row
            print(x, end=" ")
            x = x - 1
        print()

if __name__ == "__main__":                                                 
    try:
        number = int(input("Enter the number of rows:- "))            #input from user             
        if number <= 0:                                         # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")
        
        design(number)                                           # execution of function
    except ValueError:                                            # user define exeption handling; for strings input   
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")