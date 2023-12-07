def sum_matrix(A,B):
    M=len(A)
    N=len(A[0])
    C=[[0]*N for i in range (M)]
    for i in range(M):
        for j in range(N):
            C[i][j]=A[i][j]+B[i][j]
    return C
    
A=[
    [1,2],
    [3,4]
    ]
B=[
    [2,0],
    [4,3]
]
C = sum_matrix(A,B)
print (C)

def mult_matrix(A,k):
    M=len(A)
    N=len(A[0])
    C=[[0]*N for i in range (M)]
    for i in range(M):
        for j in range(N):
            C[i][j]=A[i][j]*k
    return C
    
k=5
A=[
    [1,2],
    [3,4]
    ]

C = mult_matrix(A,k)
print (C)

def multi_matrix(A,B):
    A_Rows=len(A)
    A_Cols=len(A[0])
    B_Rows=len(B)
    B_Cols=len(B[0])
    
    if(A_Cols != B_Rows):
        print('')
        return
    
    C=[[0 for row in range(B_Cols)] for col in range(A_Rows)]
    for i in range(A_Rows):
        for j in range(B_Cols):
            for k in range(A_Cols):
                C[i][j]+=A[i][k]*B[k][j]
    return C
    
A=[
    [2,1],
    [4,3],
    [5,6]

    ]
B=[
    [1,2,3],
    [3,4,5]
]
C = multi_matrix(A,B)
print (C)

def transp_matrix(A):
    M = len(A)
    N = len(A[0])
    C = [[0]*N for i in range(M)]
    for i in range(N):
        for j in range(M):
            C[i][j] = A[j][i]
    return C 

A=[
    [2,1],
    [4,3],
    [5,6]

    ]
    
C = transp_matrix(A)
print (C)
    