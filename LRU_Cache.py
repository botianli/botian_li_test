import collections

class Cache:

    def __init__(self,location,capacity=5): #initilize a cache object
        self.locat=location #location attribute
        self.list=collections.OrderedDict() #using ordered dictionary to store cache
        self.cap=capacity #capacity default is 5


    def get(self,key): #return value in cache
        try:

         value=self.list.pop(key) #to make sure LRU, popup the key then insert back, take O(1)

         self.list[key]=value
         return value
        except KeyError:
         print("Value dose not exist.")

    def set(self,key,value):
        try:
            self.list.pop(key) #in order to maintain least recently used, try to pop the key
        except:
            if len(self.list)>= self.cap: #if key doesn't exist, and the list is full
                self.list.popitem(last=False) #pop out the last item

        self.list[key]=value #put item in the list

    def __contains__(self,key):
        try:
            self.list.get(key)
            return True
        except KeyError:
            return False

    def keys(self): #return list of keys

        list=self.list.copy()
        return list

    def getcapacity(self):
        return self.cap
    def values(self): #return list of values
        return self.list.values()
    def location(self): #return location of the cache
        return self.locat
    def clear(self): #clear content in the cache
        self.list.clear()



