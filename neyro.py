import random 
import math
def sigma(x):
    return 1/ (1+math.exp(-x))
def f_activate(O):
    result = [[0] for M in range(len(O))]
    for i in range(len(O)):
        result[i][0] = sigma(O[i][0]) 
    return result  
    
def mult(A,B):
    A_rows = len(A)
    A_cols = len(A[0])
    B_rows = len(B)
    B_cols = len(B[0])

    C =[[0 for row in range(B_cols)] for col in range(A_rows)]
    for i in range(A_rows):
        for j in range(B_cols):
            for k in range(A_cols):
                C[i][j] += A[i][k] * B[k][j]
    return C
    
class NerualNetwork:

    
    def __init__(self, i_nodes, h_nodes, o_nodes,lr):
        self.__input_nodes = i_nodes
        self.__hidden_nodes = h_nodes
        self.__output_nodes = o_nodes
        self.__learning_rate = lr
        
        self.W_i_h = [[0]*i_nodes for i in range (h_nodes)]
                 
        for i in range (h_nodes):
            for j in range (i_nodes):
                self.W_i_h[i][j] = random.random()
                
        self.W_h_o = [[0]*h_nodes for i in range (o_nodes)]    
        for i in range (o_nodes):
            for j in range (h_nodes):
                self.W_h_o[i][j] = random.random()
        
        
    def query(self, inputs):
        O_h = f_activate(mult(self.W_i_h, inputs))
        O_o = f_activate(mult(self.W_h_o, O_h))
        return O_o


I= [[0.07], [0.3]]
random.seed(42)
net=NerualNetwork(2,4,1,0.1)
print (net.query(I))