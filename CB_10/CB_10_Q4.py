str = "asdfaaaabbbcttavvffffdf"  
word, temp = "", str[0]  # temp = str[0] for fence post problem
for i in range(1, len(str)):  # starting from 1 not zero because we already add first char
    x = temp[-1]  # last word in var temp
    y = str[i]  # index in for-loop
    if x <= y:
        temp += str[i]
    elif x > y:
        if len(temp) > len(word):  #storing longest substring 
            word = temp
        temp = str[i]  #reseting var temp with last char in loop
    if len(temp) > len(word):
        word = temp
print("Longest substring in alphabetical order is:", word)