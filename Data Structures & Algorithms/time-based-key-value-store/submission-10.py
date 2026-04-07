class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        store = self.store
        if store.get(key) == None:
            store[key] = [[value, timestamp]]
        else:
            store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        store = self.store.get(key, [])
        res = ""

        l, r = 0, len(store) - 1

        while l <= r:
            mid = (l + r) //2
            if store[mid][1] <= timestamp:
                res = store[mid][0]
                l = mid + 1 
            else:
                r = mid - 1
        
        return res

