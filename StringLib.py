def is_valid(input): #method to check if two string is valide version string
    try:
        lt = input.split(".") #if able to split the string
        for num in lt: #check wheather each element in the list is a digit

            if num.isdigit() == False: 
                return False
        return True
    except: #if catch any exception, means its not valid
        return False


def CompareTwoString(a,b): #method to compare to version string

    if is_valid(a) and is_valid(b):
        lt1 = a.split(".")
        lt2 = b.split(".")

        if len(lt1) == len(lt2): #if 2 string have the same length, compare them elemnt bny element
            end = 0
            for (d1, d2) in zip(lt1, lt2):

                if (d1 == d2):
                    end = end + 1
                    continue
                if (d1 > d2):  #if find one digit not the same break immediatlt then return the result
                    print(f"{a} is greater than {b}")
                    break
                if (d1 < d2):
                    print(f"{a} is less than {b}")
                    break
            if (end == len(lt1)):
                print(f"{a} is equal to {b}")
        else:

            same = 0;  #if they dont have the same length, iterate length is the one with the less length
            length1 = len(lt1)
            length2 = len(lt2)
            for i in range(min(length1, length2)):
                d1 = lt1[i]
                d2 = lt2[i]
                if (d1 > d2):  #same as above
                    same = same + 1
                    print(f"{a} is greater than {b}")
                    break
                if (d1 < d2):
                    same = same + 1
                    print(f"{a} is less than {b}")
                    break
                if (d1 == d2):
                    continue

            if (same == 0): #if they are equal, the string with the longer length is greater than the one with less length
              if (length1 > length2):
                 print(f"{a} is greater than {b}")
              else:
                  print(f"{a} is less than {b}")



    else:
        print("The input is invalid, try again.")   #if two string is not valide, return this message to user
