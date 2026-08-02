class TimeMap: 
    def __init__(self):
        self.store = {} #key=string, value=[list of [value, timestamp]]

    def set(self, key:str, value:str, timestamp: str) -> None: 
        if key not in self.store: 
            self.store[key] = [] #if the key doesn't already exist in the hashmap
            #we take the key and store it in an empty list in the hashmap
        self.store[key].append([value, timestamp]) #then, to that key we append the
                                                    #value and timestamp 

    def get(self, key:str, timestamp: int) -> str: 
        res ="" #if key doesn't exist in map we want to return empty string which is why
        #we initialize it this way
        values = self.store.get(key, [])

        #binary search 

        l = 0 
        r = len(values) - 1
        while l <= r:
            m = (l + r ) // 2
            if values[m][1] <= timestamp: 
                res = values[m][0]
                l = m + 1
            else: 
                r = m - 1
        return res