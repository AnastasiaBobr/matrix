import random
import math
def sigma(x):
    return 1/ (1+math.exp(-x))
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
    
def f_activation(O):
    result = [[0] for M in range(len(O))]
    for i in range(len(O)):
        result[i][0] = sigma(O[i][0]) 
    return result  
def vich(A,k):
    M = len(A)
    N = len(A[0])
    C=[[0]*N for i in range(M)]
    for i in range(M):
        for j in range(N):
            C[i][j] = k - A[i][j] 
    return C
def Sub(A,B):
    M = len(A)
    N = len (A[0])
    C = [[0] * N for _ in range (M)]
    
    for i in range(M):
        for j in range (N):
            C[i][j] = A[i][j] - B[i][j]            
    return C

def transp(A):
    M = len(A)
    N = len(A[0])
    
    C = [[0]*M for i in range(N)]
    for i in range(N):
      for j in range(M):
            C[i][j] = A[j][i]         
    return C
    
def skalyar(A, B):
    C = [[0]*len(B[0]) for i in range(len(A))]
    A_rows = len(A)
    A_cols = len(A[0])
    B_rows = len(B)
    B_cols = len(B[0])
    
    if (A_cols !=  B_rows):
        print ('количетсво стоблцов из 1 матрицы не равны количеству строк из 2 матрицы')
        return 

    C =[[0 for row in range(B_cols)] for col in range(A_rows)]
    for i in range(A_rows):
        for j in range(B_cols):
            for k in range(A_cols):                       
                C[i][j] += A[i][k] * B[k][j]
    return C
    
def mult_const_matrix(A,k):
    M = len(A)
    N = len(A[0])
    C=[[0]*N for i in range(M)]
    for i in range(M):
        for j in range(N):
            C[i][j] = A[i][j] *k
    return C
    
def mult_matrix(A,B):
    M = len(A)
    N = len(A[0])
    C=[[0]*N for i in range(M)]
    for i in range(M):
        for j in range(N):
            C[i][j] += A[i][j] *B[i][j]
    return C

def summ_matrix(A,B):
    M = len(A)
    N = len (A[0])
    C = [[0] * N for _ in range (M)]
    
    for i in range(M):
        for j in range (N):
            C[i][j] = A[i][j] + B[i][j]
            
    return C

k = 0.1
I= [[0.1], [0.05], [0.2]]
t= [[0.8], [0.42], [0.5]]

W_i_h = [[0]*3 for i in range (3)]
W_h_o = [[0]*3 for i in range(3)]

random.seed(42)
for i in range (3):
    for j in range (3):
        W_i_h[i][j] = random.random()  
for i in range (3):
    for j in range (3):
        W_h_o[i][j] = random.random()
        
for i in range (1000):
    O_h = f_activation(mult(W_i_h,I))
    O_o = f_activation(mult(W_h_o,O_h))
    E_o = Sub (t, O_o)
    E_h=skalyar (transp(W_h_o), E_o)
    W_h_o = mult_const_matrix(mult(mult_matrix(E_o, mult_matrix(O_o, vich(O_o, 1))), transp(O_h)), k)
    W_i_h = mult_const_matrix(mult(mult_matrix(E_h, mult_matrix(O_h, vich(O_h, 1))), transp(I)), k)
print(O_o)

dW_h_o = [[0]*3 for i in range (3)]
dW_h_o = mult_const_matrix(mult(mult_matrix(E_o, mult_matrix(O_o, vich(O_o, 1))), transp(O_h)), k)
#print(dW_h_o)

dW_i_h = [[0]*3 for i in range (3)]
dW_i_h = mult_const_matrix(mult(mult_matrix(E_h, mult_matrix(O_h, vich(O_h, 1))), transp(I)), k)
#print(dW_i_h)

W_h_o = summ_matrix(W_h_o, dW_h_o)
#print (W_h_o)

W_i_h = summ_matrix(W_i_h, dW_i_h)
#print (W_i_h)