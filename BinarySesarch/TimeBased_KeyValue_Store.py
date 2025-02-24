from collections import defaultdict
class TimeMap(object):
# can do a binary search for the get 
# for set method, we can use a timeseries array and store tuples in it since we don't need to modify the data
    def __init__(self):
        # timeseries = []
        self.timeseries = defaultdict(list) # key=string, value = [list of [value, timestamp]]
    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.timeseries[key].append([value,timestamp])
        # Concatenate a list containing the new tuple to the existing list
        # self.timeseries[key] += [(value, timestamp)]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        # look for maxtimestamp that has the key
        # print(self.timeseries)


        values = self.timeseries.get(key,[])

        # binary search
        l, r = 0, len(values) -1

        while l <= r: 
            mid = (l+r)//2 

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1


        return res

### my solution without parsing out the key array into a seperate value

        # res = ""

        # if self.timeseries:
        #     # binary search
        #     l, r = 0, len(self.timeseries[key]) -1

        #     while l <= r: 
        #         mid = (l+r)//2 

        #         if self.timeseries[key][mid][1] <= timestamp:
        #             res =  self.timeseries[key][mid][0]
        #             l = mid + 1
        #         else:
        #             r = mid - 1


        # return res

# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)