'''
Created on Mar 28, 2015

@author: hustnn
'''


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
        
        
    def getCapacity(self):
        return self._capacity