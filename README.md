# botian_li_test
based on python version 3.8.1

Line.py: Contain Method overlap
test result:
line:(4, 5) and line(2, 6) overlapping result is:
True

line:(2, 6) and line(2, 7) overlapping result is:
True

line:(8, 10) and line(10, 11) overlapping result is:
False

line:(-1, 3) and line(2, 7) overlapping result is:
True

line:(4, 5) and line(2, 7) overlapping result is:
True


StringLib: Module that have a CompareTwoString function\n

Q2_tester: tester for Q2, showing how error is being handled

test result:

10 is equal to 10

1.1 is greater than 0

1.1.1 is greater than 1

The input is invalid, try again.

1.1.1 is less than 1.2

1.2.1 is greater than 1

Q3 LRU_Cache:

The cache is identified by location name, To have LRU cache, I set default capacity to  5 for easy testing purpose.
I use ordered dictionary to tract the least used key.  get(key) method will rearrange order in the dictionary so that if list is at max capacity, the last item we popout is always the least being used. In Q3_test, I have a little tester to test that.
