'''
Created on Mar 28, 2015

@author: hustnn
'''

import numpy
from itertools import product

from WeightOps import WeightOps

import threading
import math
import time
import multiprocessing

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
    def bruteForcePack(cls, containerWeights, numOfContainers, groups, packResults, minV, maxV):    
        boxesNumList = []
        for g in groups:
            boxesNumList.append(range(g.getSize() + 1))
            
        combinations = []
        for combination in product(*boxesNumList):
            num = 0
            for i in combination:
                if i == 1:
                    num += 1
                    
            if num >= minV and num <= maxV:
                combinations.append(combination)
            
        for combination in combinations:
            if cls.satisfy(containerWeights, groups, combination):
                #print(combination)
                # copy the groups
                cloneGroups = [g.clone() for g in groups]
                for i in range(len(combination)):
                    cloneGroups[i].removeBox(combination[i])
                    
                selectedGroups =  [g for g in cloneGroups if g.getSize() > 0]
                    
                if cls.allFinished(selectedGroups):
                    packResults.put(numOfContainers)
                else:
                    cls.bruteForcePack(containerWeights, numOfContainers + 1, selectedGroups, packResults, min(minV, len(selectedGroups)), maxV)
                  
                  
    @classmethod
    def multiThreadPack(cls, combinations, packResults, containerWeights, groups, minV, maxV):
        #print(combinations)
        #print("begin")
        for combination in combinations:
            if cls.satisfy(containerWeights, groups, combination):
                cloneGroups = [g.clone() for g in groups]
                for i in range(len(combination)):
                    cloneGroups[i].removeBox(combination[i])
                    
                selectedGroups =  [g for g in cloneGroups if g.getSize() > 0]
                    
                if cls.allFinished(selectedGroups):
                    packResults.put(1)
                else:
                    cls.bruteForcePack(containerWeights, 2, selectedGroups, packResults, min(minV, len(selectedGroups)), maxV)
      
    '''               
    @classmethod
    def multiThreadProc(cls, containerWeights, groups):
        boxesNumList = []
        for g in groups:
            boxesNumList.append(range(g.getSize() + 1))
            
        combinations = []
        for combination in product(*boxesNumList):
            combinations.append(combination)
            
        res = []
        threadList = []
        
        totalLen = len(combinations)
        totalThread = 1024
        lenPerThread = int(math.ceil(float(totalLen) / totalThread))
        threadNum = 0
        
        for i in range(totalThread):
            begin = i * lenPerThread
            end = min(begin + lenPerThread, totalLen)
            partCombinations = combinations[begin:end]
            threadNum += 1
            res.append([])
            t = threading.Thread(target = cls.multiThreadPack, args = (partCombinations, res[threadNum - 1], containerWeights, groups,))
            threadList.append(t)
            if end == totalLen:
                break
            
        for t in threadList:
            t.start()
            #time.sleep(0.1)
            
        for t in threadList:
            t.join()
        
        return res'''
    
    
    @classmethod
    def multiProcess(cls, containerWeights, groups, numOfProcess, minV, maxV):
        boxesNumList = []
        for g in groups:
            boxesNumList.append(range(g.getSize() + 1))
            
        combinations = []
        for combination in product(*boxesNumList):
            num = 0
            for i in combination:
                if i == 1:
                    num += 1
                    
            if num >= minV and num <= maxV:
                combinations.append(combination)
            
        #print(combinations)
            
        res = []
        processList = []
        
        totalLen = len(combinations)
        processNum = numOfProcess
        lenPerProc = int(math.ceil(float(totalLen) / processNum))
        procNum = 0
        
        for i in range(processNum):
            begin = i * lenPerProc
            end = min(begin + lenPerProc, totalLen)
            partCombinations = combinations[begin:end]
            procNum += 1
            res.append(multiprocessing.Queue())
            p = multiprocessing.Process(target = cls.multiThreadPack, 
                                        args = (partCombinations, res[procNum - 1], containerWeights, groups, min(minV, len(groups)), maxV))
            processList.append(p)
            if end == totalLen:
                break    
        
        for p in processList:
            p.start()
            time.sleep(1)
            
        for p in processList:
            p.join()
            
        return res
    
    
    @classmethod
    def loop(cls, threadName):
        print(threadName)
        for i in range(1000000000):
            pass
        
    
    @classmethod
    def threadTest(cls):
        threadList = []
        for i in range(5):
            t = threading.Thread(target = cls.loop, args = (str(i),))
            threadList.append(t)
            
        for t in threadList:
            t.start()
            
        for t in threadList:
            t.join()
            
                    
    @staticmethod
    def allFinished(groups):
        return len(groups) == 0
        
            
    @staticmethod
    def satisfy(containerWeights, groups, combination):
        boxesWeights = [0] * len(groups[0].getBoxWeights())
        
        for i in range(len(combination)):
            num = combination[i]
            boxWeight = WeightOps.scaleOfWeight(groups[i].getBoxWeights(), num) 
            boxesWeights = WeightOps.add(boxesWeights, boxWeight)
            
        if not WeightOps.fitIn(boxesWeights, containerWeights):
            return False
        
        cloneGroups = [g.clone() for g in groups]
        for i in range(len(combination)):
            cloneGroups[i].removeBox(combination[i])
        
        if len([g for g in cloneGroups if g.getSize() > 0]) == 0:
            return True
        
        for g in cloneGroups:
            if g.getSize() >= 1:
                weights = WeightOps.add(boxesWeights, g.getBoxWeights())
                if not WeightOps.fitIn(weights, containerWeights):
                    return True
                
        return False
            