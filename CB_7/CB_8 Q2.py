#Test Cases
#input==19
#Input=7
#input=11
#input=31


#printting the upper diagram
def print_pattern(number):
    input=number
    rows=(input-1)//2
    spaces=rows*3
    inner_diagram=1
    for i in range(1,rows+1):
        print("-"*spaces,end="")
        print(".|."*inner_diagram,end="")
        inner_diagram+=2
        print("-"*spaces,end="\n")
        spaces-=3

# printting the Welcome name
    welcome=((input*3)//2)-3
    print(welcome*"-"+"WELCOME"+"-"*welcome)
    inner_diagram-=2
    spaces+=3



#Loop for printing the Bottom diagram
    for j in range(1,rows+1):
        print("-"*spaces,end="")
        print(".|."*inner_diagram,end="")
        inner_diagram-=2
        print("-"*spaces,end="\n")
        spaces+=3


if __name__ == "__main__":
    try:
        
        
        print(end="\n")
        number = int(input("Enter the number greater than 3 and must be odd number:- "))
        type = type(number)
        if number > 3 & number%2==1:
            print_pattern(number)
        elif number>3 & number%2==0:
            print("You enter the even number!!!!!!!!!")

        elif number <= 0:
            print("Input should't be negative or zero. Please Enter positive number.")
    except ValueError:  # user define exeption handling;
        print("Input should not be string. Please Enter positive number.")
    finally:
        print("Program ended..................................")

