'''
Created on Mar 28, 2015

@author: hustnn
'''

import numpy
from WeightOps import WeightOps


class KnapsackOps(object):
    '''
    classdocs
    '''

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