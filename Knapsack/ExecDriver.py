'''
Created on Mar 27, 2015

@author: hustnn
'''

from Capacity import Capacity
from CapacityOps import CapacityOps
from Container import Container
from KnapsackOps import KnapsackOps
from Box import Box
from Group import Group

if __name__ == '__main__':
    containerCapacity = Capacity(2, 2)
    #print(containerCapacity.getWeights())
    
    container = Container(containerCapacity)
     
    capacity1 = Capacity(1, 1)
    boxes1 = [Box(1, CapacityOps.clone(capacity1)), Box(2, CapacityOps.clone(capacity1))]
    group1 = Group(1, boxes1)
    
    groups = [group1]
    
    KnapsackOps.Pack(container, groups)