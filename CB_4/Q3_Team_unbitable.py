def star(number):
    for i in range(1, number+1):                     #for first upper half of pattern
        print(i*'*', end=' ')
        print()
    for i in range(number-1,0,-1):                  #for lower part of pattern
        print(i*'*', end=' ')
        print()

if __name__ == "__main__":                                                 
    try:
        number = int(input("Enter the number of rows:- "))            #input from user             
        if number <= 0:                                         # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")
        
        star(number)                                           # execution of function
    except ValueError:                                            # user define exeption handling; for strings input   
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")