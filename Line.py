class Line:


    def overlape(line1,line2): #here I assume the input is valid with the form line1=(x1,x2) line2=(x3,x4)
        b1=min(line1[0],line1[1])
        e1=max(line1[0],line1[1])
        b2 = min(line2[0], line2[1])
        e2 = max(line2[0], line2[1])
        if(b2<e1 and e1<=e2): #first case: one line is over lap with the end of the other line
           return True

        if(b1<=b2 and e2<=e1 ): #second case: one line is over lap with the beginning of the other line
             return True
        if(b2<=b1 and e2>b1): #third case: one line is within another line
             return True
        else:
             return False


    line1=(4,5)
    line2=(2,6)
    line3=(-1,3)
    line4=(2,7)
    line5=(8,10)
    line6=(10,11)
    test1=(line1,line2)
    test2=(line3,line4)
    test3=(line1,line4)
    test4=(line2,line4)
    test5=(line5,line6)

    test_list={test1,test2,test3,test4,test5}
    for test in test_list:
        print(f"line:{test[0]} and line{test[1]} overlapping result is:")
        print(overlape(test[0],test[1]))



