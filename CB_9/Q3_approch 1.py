def printLikeStatus(lengthOfArray, likes):

    if lengthOfArray <= 3:  # loop for arrray if length is 3 or less than 3.
        for i in range(0, lengthOfArray):
            if lengthOfArray-1 == i:  # if array contains only one like.
                print(likes[i], "like this.")
            # if array element is last out of three.
            elif i == lengthOfArray-1:
                print("and", likes[i], "like this .", end=" ")
            # if array element is second-last out of three.
            elif i == lengthOfArray-2:
                print(likes[i], end=" ")

    else:
        # loop for length is more than 3 to infinite.
        for i in range(0, lengthOfArray):
            if i == 0:
                print(likes[i], ",", end="")
            elif i == 2:
                print(likes[i], end=" ")

        print("and", lengthOfArray-2, "others like this.")

if __name__ == "__main__":

    likes = ['abhishek', 'piyush', 'kishor', 'pranav', 'vivek']  # static part.
    # dynamic array part.
    # likes = []
    # choice = True
    # while choice == True:
    #     like = input(" Plese enter the name ")
    #     likes.append(like)
    #     userChoice = int(
    #         input("Do you want to add more names press 1 for yes  2 for no "))

    #     if userChoice == 1:
    #         choice == True
    #     elif userChoice == 2:
    #         print("printing msg")
    #         break
    #     else:
    #         print("you enter the key which is not bind")
    #         break

    lengthOfArray = len(likes)
    print(lengthOfArray)
    printLikeStatus(lengthOfArray, likes)



