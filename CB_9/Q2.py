def findUnique(set):
    lengthOfset = len(set)
    print(lengthOfset)
    uniqueSet = []
    repeatValue = 0

    for i in range(0, lengthOfset):
        for j in range(0, lengthOfset):
            if i != j:
                if set[i] == set[j]:
                    repeatValue = repeatValue+1

        if repeatValue == 0:
            uniqueSet.append(set[i])
        else:
            repeatValue = 0
    print("unique array is following")
    print(uniqueSet)


if __name__ == "__main__":
    set = [1, 2, 0.5, 0, 0, 2, 2, 3, 3, 4, 5, 5, 6, 6, 1, 4, 'a', 'a', 'b']
    findUnique(set)
