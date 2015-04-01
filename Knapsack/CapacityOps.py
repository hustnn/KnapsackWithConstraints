'''
Created on Mar 28, 2015

@author: hustnn
'''

from Capacity import Capacity

class CapacityOps(object):
    '''
    classdocs
    '''


    @staticmethod
    def clone(capacity):
        return Capacity(*(capacity.getWeights()))
    
    '''
    @staticmethod
    def addTo(l, r):
        if len(l.getWeights()) != len(r.getWeights()):
            raise Exception("different dimension")
        else:
            lWeights = l.getWeights()
            rWeights = r.getWeight()
            for i in range(len(lWeights)):
                lWeights[i] += rWeights[i]
                
                
    @staticmethod
    def substractFrom(l, r):
        if len(l.getWeights()) != len(r.getWeights()):
            raise Exception("different dimension")
        else:
            lWeights = l.getWeights()
            rWeights = r.getWeight()
            for i in range(len(lWeights)):
                lWeights[i] -= rWeights[i]
                
    
                
                
    @staticmethod
    def fitIn(tar, des):
        if len(tar.getWeights()) != len(des.getWeights()):
            return False
        else:
            tarWeights = tar.getWeights()
            desWeights = des.getWeights()
            for i in range(len(tarWeights)):
                if tarWeights[i] > desWeights[i]:
                    return False
            return True'''