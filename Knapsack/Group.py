'''
Created on Mar 27, 2015

@author: hustnn
'''

from WeightOps import WeightOps

class Group(object):
    '''
    classdocs
    '''


    def __init__(self, groupID, size, weights):
        '''
        Constructor
        '''
        self._groupID = groupID
        self._size = size
        #self._boxes = boxes
        #self._boxWeights = WeightOps.clone(boxes[0].getWeights())
        self._weights = weights
        
        
    def removeBox(self, size):
        #self._boxes.remove(box)
        self._size -= size
        
        
    def getSize(self):
        return self._size
    
    
    def getBoxes(self):
        return self._boxes
    
    
    def getBoxWeights(self):
        return self._weights
    
    
    def clone(self):
        return Group(self._groupID, self._size, self._weights)