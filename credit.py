

def main():
    number = input("Number: ")

    # start, stop (exclusive), end
    # mult by 2 and add individual digits to sum, start at num before last
    multSum = 0
    for i in range(len(number) - 2, -1, -2):
        num = int(number[i]) * 2

        # convert to str and add individual digits
        if (num > 9):
            num = str(num)
            multSum += int(num[0]) + int(num[1])
        else:
            num = str(num)
            multSum += int(num[0])


    #now add un multed nums
    addSum = 0
    for i in range(len(number)-1, -1, -2):
        addSum += int(number[i])

    if((multSum + addSum) % 10 != 0):
        print("INVALID")
        return

    # if number is valid, then check what model it is by inspecting its vals
    match number[0]:
        case '3':
            print("ok")

main()