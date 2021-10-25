    

def expert():                                      # function

    try:                                       
        ls=[0, 1, 3, 6, 10]                     
        nl=[]                                   
        print("List: ", ls)
        for x in range(0,len(ls)):
            nl.append(sum(ls)) 
            ls.pop(0)
            if len(ls)==0:
                nl.append(0)

        print("\n Sum of parts of list put together in a new list: ", nl)       
    except: 
        print("==== ERROR OCCURED ====")
        
expert()



