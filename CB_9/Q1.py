def ascendingOdds(array):
    odds = []
    for i in array:
        if i%2 != 0:
            odds.append(i)                                 # collecting odd numbers
    odds.sort()
    for i in range(len(array)):
        if array[i] % 2 == 0:
            odds.insert(i, array[i])                       # inserting even numbers at their original position
    return odds
    
if __name__ == "__main__":
    array = []
    numbers = input('enter comma(,) separted numbers :- ')
    if numbers:
        try:
            array = numbers.split(',')
            array = list(map(int, array))
            print(ascendingOdds(array))                # execution of function
        except:
            print('enter comma separated numbers like 1,2,3,4,5')
    else:
        print('please enter some numbers to execute function')
    print("Program ended..................................")
