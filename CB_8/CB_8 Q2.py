def func1():                                   

    try:                                          
        n= str(int(input("Enter any number string : ")))
        if n[0]=="-":
            print("-"+"".join(reversed(n[1:])))
        else:
            print("".join(reversed(n)))
    except: 
        print("ERROR OCCURED")
func1()