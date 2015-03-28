'''
Created on Mar 27, 2015

@author: hustnn
'''

import numpy

class Capacity(object):
    '''
    classdocs
    '''


    def __init__(self, *capacity):
        '''
        Constructor
        '''
        self._weights = []
        for c in capacity:
            self._weights.append(c)
            
            
    def getWeights(self):
        return self._weights
    
    
    def __hash__(self):
        w = tuple(self._weights)
        return hash(w)
    
    
    def __eq__(self, other):
        selfWeight = tuple(self._weights)
        otherWeight = tuple(other.getWeights())
        return selfWeight == otherWeight
        
    
    