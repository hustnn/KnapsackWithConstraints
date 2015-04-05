'''
Created on Mar 28, 2015

@author: hustnn
'''

import numpy
from itertools import product

from WeightOps import WeightOps


class KnapsackOps(object):
    '''
    classdocs
    '''
    packResults = []

    @staticmethod
    def Pack(container, groups):
        f = {}
        # init with any capacity combination
        dimension = container.getCapacity().getWeights()
        dimensionExt = [i + 1 for i in dimension]
        f[0] = numpy.zeros(dimensionExt)
        for i in range(1, len(groups) + 1):
            currentGroup = groups[i - 1]
            n = currentGroup.getSize() # the number of boxes in the current group
            f[i] = numpy.zeros(dimensionExt)
            for index, value in numpy.ndenumerate(f[0]):
                curContainerWeights = list(index)
                maxProfit = 0
                if n > 0:
                    boxWeights = currentGroup.getBoxes()[0].getWeights()
                    boxProfit = currentGroup.getBoxes()[0].getProfit()
                else:
                    boxWeights = [0] * len(dimension)
                    boxProfit = 0
                for k in range(n + 1):
                    totalBoxWeights = WeightOps.scaleOfWeight(boxWeights, k) # the sum of k boxes
                    if WeightOps.fitIn(totalBoxWeights, curContainerWeights):
                        leftWeights = WeightOps.substract(curContainerWeights, totalBoxWeights)
                        maxProfit = max(maxProfit, f[i - 1][tuple(leftWeights)] + boxProfit * k)
                f[i][tuple(curContainerWeights)] = maxProfit
        
        res = f[len(groups)][tuple(dimension)]
        print(res)
        
    
    @classmethod
    def bruteForcePack(cls, containerWeights, numOfContainers, groups):    
        selectedGroups =  [g for g in groups if g.getSize() > 0]
        boxesNumList = []
        for g in selectedGroups:
            boxesNumList.append(range(g.getSize() + 1))
            
        for combination in product(*boxesNumList):
            if cls.satisfy(containerWeights, selectedGroups, combination):
                # copy the groups
                cloneGroups = [g.clone() for g in selectedGroups]
                for i in range(len(combination)):
                    cloneGroups[i].removeBox(combination[i])
                    
                if cls.allFinished(cloneGroups):
                    print("finished")
                    cls.packResults.append(numOfContainers)
                else:
                    cls.bruteForcePack(containerWeights, numOfContainers + 1, cloneGroups)
                    
                    
    @staticmethod
    def allFinished(groups):
        return len([g for g in groups if g.getSize() > 0]) == 0
        
            
    @staticmethod
    def satisfy(containerWeights, groups, combination):
        boxesWeights = [0] * len(groups[0].getBoxWeights())
        
        for i in range(len(combination)):
            num = combination[i]
            boxWeight = WeightOps.scaleOfWeight(groups[i].getBoxWeights(), num) 
            boxesWeights = WeightOps.add(boxesWeights, boxWeight)
            
        if not WeightOps.fitIn(boxesWeights, containerWeights):
            return False
        
        if len([g for g in groups if g.getSize() > 0]) == 0:
            return True
        
        for g in groups:
            if g.getSize() >= 1:
                weights = WeightOps.add(boxesWeights, g.getBoxWeights())
                if not WeightOps.fitIn(weights, containerWeights):
                    return True
                
        return False
            