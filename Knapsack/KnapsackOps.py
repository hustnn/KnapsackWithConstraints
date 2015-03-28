'''
Created on Mar 28, 2015

@author: hustnn
'''

import numpy


class KnapsackOps(object):
    '''
    classdocs
    '''


    @staticmethod
    def pack(container, groups):
         f = {}
         # init with any capacity combination
         f[0] = numpy.zeros(container.getWeights())
         