from StringLib import CompareTwoString


def main():
  a='10'
  b='10'
  CompareTwoString(a,b)
  a="1.1"
  b="0"
  CompareTwoString(a, b)
  a = "1.1.1"
  b = "1"
  CompareTwoString(a,b)
  a="a"
  b="b"
  CompareTwoString(a,b)
  a = "1.1,1"
  b = "1"
  CompareTwoString(a, b)



if __name__=='__main__':
    main()
