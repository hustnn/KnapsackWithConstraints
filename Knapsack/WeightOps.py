'''
Created on Apr 1, 2015

@author: hustnn
'''

class WeightOps(object):
    '''
    classdocs
    '''


    @staticmethod
    def clone(weight):
        return list(weight)
    
    
    @staticmethod
    def fitIn(tar, des):
        if len(tar) != len(des):
            raise Exception("different length")
        for i in range(len(tar)):
            if tar[i] > des[i]:
                return False
        return True
    
    
    @staticmethod
    def substract(l, r):
        if len(l) != len(r):
            raise Exception("different length")
        res = list(l)
        for i in range(len(l)):
            res[i] -= r[i]
        return res
    
    
    @staticmethod
    def scaleOfWeight(weights, scale):
        res = []
        for i in weights:
            res.append(i * scale)
        return res