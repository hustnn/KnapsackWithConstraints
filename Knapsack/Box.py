'''
Created on Mar 27, 2015

@author: hustnn
'''

from Capacity import Capacity

class Box(object):
    '''
    classdocs
    '''
    def __init__(self, boxID, capacity):
        '''
        Constructor
        '''
        self._boxID = boxID
        self._capacity = capacity
        
        
    def getWeights(self):
        return self._capacity.getWeights()
    
        
    def getProfit(self):
        p = 1.0
        for i in self._capacity.getWeights():
            p *= i
        return p
        