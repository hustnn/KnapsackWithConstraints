'''
Created on Mar 28, 2015

@author: hustnn
'''

from Capacity import Capacity

class Container(object):
    '''
    classdocs
    '''


    def __init__(self, capacity):
        '''
        Constructor
        '''
        self._capacity = capacity
        self._leftCapacity = capacity
        
        
    def getWeights(self):
        return tuple(self._capacity.getWeights())