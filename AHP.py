#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 19:10:25 2019

@author: guinther
"""
import numpy as np

class ahp():
    def __init__(self,size): 
        RI_saaty = [0.58,0.9,1.124,1.32,1.41,1.48,1.49]
        self.M = np.ones((size,size))
        self.OPTIONS = []
        self.W = []
        self.DECISION = []
        self.CONSISTENCY = 0
        self.C = 0
        self.RI = RI_saaty[size-3]   
        
    def options(self):   
        for i in range(len(self.M)):
            self.OPTIONS.append(input('OPÇÃO: '+str(i)+'\n'))
        return self.OPTIONS
    
    def decision(self):
        self.W = []
        for i in range(self.M.shape[0]):
            for j in range(self.M.shape[0]):
                if i<j:
                    INPUT = float(input(str(self.OPTIONS[i])+'>'+str(self.OPTIONS[j])+'\n'))
                    if INPUT<0:
                        INPUT = 1/abs(INPUT)
                    self.M[i,j]=INPUT
        self.M = self.M.T+self.M-1
        
        for i in range(self.M.shape[0]):
            self.M[:,i] = self.M[:,i]/(self.M[:,i].sum())
        
        for i in range(self.M.shape[0]):
            self.DECISION.append((round(self.M[i,:].sum()/self.M.shape[0],3),self.OPTIONS[i]))
            self.W.append((self.M[i,:].sum()/self.M.shape[0]))
        #print('Decision')
        #print(np.array(self.DECISION))
    
    def consistency(self):
        WEIGHT = np.array(self.W)
        self.C = np.matmul(self.M,WEIGHT)/self.W
        LAMBDA = self.C.sum()
        CI = (LAMBDA-self.M.shape[0])/(self.M.shape[0]-1)
        #print('consistency:',abs(CI/self.RI))

#import ahp
criterios = ahp(3)
criterios.options()
criterios.decision()
criterios.consistency()
pesos = []
alternativas = ahp(3)
alternativas.options()
for criterio in criterios.OPTIONS:
    print(criterio)    
    alternativas.decision()
    alternativas.consistency()
    pesos.append(escolhas.W)

print(np.matmul(criterios.W,np.array(pesos)))
print(escolhas.OPTIONS)
    
