from LRU_Cache import Cache
def main():
 cache=Cache("Montreal")
 print(f"Location is:{cache.location()}")
 print(f"Capacity is: {cache.getcapacity()}")
 Testing=(("a",20),("b",3),("c",2),("d",5),("e",204),("f",303),("z",5005), ("w",646))
 for (key,value) in tuple(Testing):
     cache.set(key,value)
     print(f"Adding key:{key}, value:{value}")

 cache_list=cache.keys()
 print(f"After adding: \n{cache_list}")


 getlist={"d","e","c"}
 for key in getlist:

     print(f"Search  key:{key}")
     value=cache.get(key)
     print(value)

 addnew=(("v",45),("p",45))
 for (key,value) in tuple(addnew):
     cache.set(key,value)
     print(f"Adding new key:{key}, value:{value}")

 print(f"After new adding,list have: \n{cache_list}")
 print("c,d is gone since they are the least recently used in the cache.")

if __name__=="__main__":
    main()