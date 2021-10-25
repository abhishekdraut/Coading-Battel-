def star(num):                       #function
    for i in range(1,num+1):                     # range for rows
        print(((num+4)-i)*"*",end="")        #code for first part of stars i.e. before numbers
        print(i*(str(i)+"*"),end="")             # code for numbers and middle stars
        print(((num+3)-i)*"*",end="")         # code for last part of stars    
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