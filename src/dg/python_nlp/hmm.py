#HMM Forward algorithm  
  
#input  Matrix A,B vector pi  
  
import  numpy as np  
  
  
A=np.array([[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]])  
B=np.array([[0.5,0.5],[0.4,0.6],[0.7,0.3]])  
O=np.array([0 ,1, 0])#T=3  
#O=np.array([1 ,0, 1])#T=3  
pi=np.array([0.2,0.4,0.4])  
  
N=3#N kind state  
M=2#M kind of observation  
T=3  
  
#initialize:  
  
Aerfa=np.zeros((3,3),np.float)  
for i in range(N):  
    Aerfa[0,i]=pi[i]*B[i,O[0]]  
  
      
#Recursion:  
for t in range(T-1):  
    for i in range(N):    
        for j in range(N):  
            Aerfa[t+1,i]+=Aerfa[t,j]*A[j,i]  
        Aerfa[t+1,i]*=B[i,O[t+1]]  
      
#compute P(O|lamda) and termination  
P=0  
for i in range(N):  
    P+=Aerfa[T-1,i]#begin with 0 so T-1  
  
          
print P  
  
  
  
  
#backward  
  
#initialize:  
Beta=np.zeros((T,N),np.float)  
print Beta  
for i in range(N):  
    Beta[T-1,i]=1  
  
#recursion:  
for t in range(T-2,-1,-1):  
    for i in range(N):  
        for j in range(N):  
            Beta[t,i]+=A[i,j]*B[j,O[t+1]]*Beta[t+1,j]  
  
              
#termination:  
P_back=0  
for i in range(N):  
    P_back+=pi[i]*B[i,O[0]]*Beta[0,i]  
      
print P_back
