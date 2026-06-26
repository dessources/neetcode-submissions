class TimeMap:

    def __init__(self):
        self.hm = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hm:
            self.hm[key].append((timestamp,value))
        else:
            self.hm[key]=[(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hm:
            arr = self.hm[key]
            l,r = 0,len(arr)-1
            val = ""
            while l<=r:
                m = (l+r)//2
                if arr[m][0] == timestamp:
                    return arr[m][1]
                if arr[m][0] > timestamp:
                    r = m - 1
                else:
                    val = arr[m][1]
                    l = m+1
            return val
        else:
            return ""