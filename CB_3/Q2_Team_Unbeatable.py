def fun(num):
    for i in range(1,num+1): # Generating pattern
        for j in range(1, num+1-i): # for space
            print(' ', end='')
    
    
        for j in range(1,i+1): # for increasing pattern
            print(j, end='')
    
    
        for j in range(i-1,0,-1): # for decreasing pattern 
            print(j, end='')
    
    
        print() # Moving to next line
   

if __name__ == "__main__":                                                 
    try:
        number = int(input("Enter the number of rows:- "))            #input from user             
        if number <= 0:                                         # for input 0 and negative numbers
            print("Input should't be negative or zero. Please Enter positive number.")
        
        fun(number)                                           # execution of function
    except ValueError:                                            # user define exeption handling; for strings input   
        print("Input should not be string. Please Enter positive number.")
    finally:                                                          # to run after every execution
        print("Program ended..................................")