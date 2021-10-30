def likes(array):
    count = len(array)
    if count == 0:                                                            # for empty array
        return 'no one likes this'
    if count == 1:
        return '{} likes this'.format(array[0])
    if count == 2:
        return '{} and {} likes this'.format(array[0], array[1])
    if count == 3:
        return '{}, {} and {} likes this'.format(array[0], array[1], array[2])
    else:
        return '{}, {} and {} others likes this'.format(array[0], array[1], (count - 2))  # counting number of rest of likes

if __name__ == "__main__":
    array = []
    string = input("Enter comma&space(', ') separated names :- ")           #input from user 
    error = False
    if string:
        array = string.split(', ')
        for name in array:
            if ',' in name:
                print('please enter names like ajay, swapnil, komal, abhishek, debabrata')
                error = True
                break
    if not error:
        print(likes(array))                         # execution of function
    print("Program ended..................................")