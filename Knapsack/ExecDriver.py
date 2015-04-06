'''
Created on Mar 27, 2015

@author: hustnn
'''

from Capacity import Capacity
from CapacityOps import CapacityOps
from WeightOps import WeightOps
from Container import Container
from KnapsackOps import KnapsackOps
from Box import Box
from Group import Group
import Config

import math

def genGroups():
    groups = []
    fileName = Config.WORKLOAD_PATH + Config.GROUP_FILE
    file = open(fileName, "r")
    lines = file.readlines()
    for line in lines:
        items = line.strip().split(",")
        group = Group(len(groups) + 1, 1, [int(w) for w in items])
        groups.append(group)
    file.close()
    return groups


def genGroupSet():
    groupSet = []
    fileName = Config.WORKLOAD_PATH + Config.GROUP_FILE
    file = open(fileName, "r")
    lines = file.readlines()
    for line in lines:
        items = line.strip().split(",")
        groupSet.append([int(w) for w in items])
    file.close()
    return groupSet


def test():
    containerCapacity = Capacity(12, 12, 12, 12)
    #print(containerCapacity.getWeights())
    
    container = Container(containerCapacity)
     
    capacity = Capacity(1, 1)
    
    boxes1 = [Box(1, CapacityOps.clone(capacity)), Box(2, CapacityOps.clone(capacity))]
    group1 = Group(1, 2, WeightOps.clone(capacity.getWeights()))
    
    boxes2 = [Box(1, CapacityOps.clone(capacity)), Box(2, CapacityOps.clone(capacity))]
    group2 = Group(2, 2, WeightOps.clone(capacity.getWeights()))
    
    groups = [group1, group2]
    
    #KnapsackOps.Pack(container, groups)
    
    KnapsackOps.bruteForcePack(containerCapacity.getWeights(), 1, groups)
    print(KnapsackOps.packResults)
    
    
def genGroupsByScale(groupSize, groupSet, groupScale):
    groups = []
    for i in range(len(groupSet)):
        begin = i * groupScale + 1
        end = (i + 1) * groupScale
        for groupID in range(begin, end + 1):
            group = Group(groupID, groupSize, groupSet[i])
            groups.append(group)
            
    return groups

    
def calPackRound(numOfContainer, containerCapacity, groupScale):
    groupSet = genGroupSet()
    groups = genGroupsByScale(1, groupSet, groupScale)
    
    KnapsackOps.bruteForcePack(containerCapacity.getWeights(), 1, groups)
    res = list(set(KnapsackOps.packResults))
    return [int(math.ceil(float(i)) / numOfContainer) for i in res]
    

if __name__ == '__main__':
    containerCapacity = Capacity(12, 12, 12, 12)
    
    #res = calPackRound(1, containerCapacity, 3)
    #print(res)
    
    groupSet = genGroupSet()
    groups = genGroupsByScale(1, groupSet, 3)
    #res = KnapsackOps.multiThreadProc(containerCapacity.getWeights(), groups)
    res = KnapsackOps.multiProcess(containerCapacity.getWeights(), groups, 32, min(2, len(groups)), 4)
    finalResult = []
    for q in res:
        while not q.empty():
            finalResult.append(q.get())
        
    print(list(set(finalResult)))
    
    #KnapsackOps.threadTest()