'''
Code snippet from Beazley and Jones in Python Cookbook 3rd edition
'''

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0 
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item)) 
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
    # additional peek function on top of the book
    def peek(self):
    
