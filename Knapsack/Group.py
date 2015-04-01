'''
Created on Mar 27, 2015

@author: hustnn
'''

class Group(object):
    '''
    classdocs
    '''


    def __init__(self, groupID, boxes):
        '''
        Constructor
        '''
        self._groupID = groupID
        self._size = len(boxes)
        self._boxes = boxes
        
        
    def removeBox(self, box):
        self._boxes.remove(box)
        self._size -= 1
        
        
    def getSize(self):
        return self._size
    
    
    def getBoxes(self):
        return self._boxes