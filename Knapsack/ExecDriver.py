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

if __name__ == '__main__':
    containerCapacity = Capacity(2, 2)
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