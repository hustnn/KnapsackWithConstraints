'''
Created on Mar 27, 2015

@author: hustnn
'''

from Capacity import Capacity

class Box(object):
    '''
    classdocs
    '''
    def __init__(self, boxID, *capacity):
        '''
        Constructor
        '''
        self._boxID = boxID
        self._capacity = Capacity(capacity)
        