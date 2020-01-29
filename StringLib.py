def is_valid(input):
    try:
        lt = input.split(".")
        for num in lt:

            if num.isdigit() == False:
                return False
        return True
    except:
        return False


def CompareTwoString(a,b):

    if is_valid(a) and is_valid(b):
        lt1 = a.split(".")
        lt2 = b.split(".")

        if len(lt1) == len(lt2):
            end = 0
            for (d1, d2) in zip(lt1, lt2):

                if (d1 == d2):
                    end = end + 1
                    continue
                if (d1 > d2):
                    print(f"{a} is greater than {b}")
                    break
                if (d1 < d2):
                    print(f"{a} is less than {b}")
                    break
            if (end == len(lt1)):
                print(f"{a} is equal to {b}")
        else:

            same = 0;
            length1 = len(lt1)
            length2 = len(lt2)
            for i in range(min(length1, length2)):
                d1 = lt1[i]
                d2 = lt2[i]
                if (d1 > d2):
                    same = same + 1
                    print(f"{a} is greater than {b}")
                    break
                if (d1 < d2):
                    same = same + 1
                    print(f"{a} is less than {b}")
                    break
                if (d1 == d2):
                    continue

            if (same == 0):
              if (length1 > length2):
                 print(f"{a} is greater than {b}")
              else:
                  print(f"{a} is less than {b}")



    else:
        print("The input is invalid, try again.")
