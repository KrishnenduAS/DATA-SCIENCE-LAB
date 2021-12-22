import matplotlib.pyplot as plt
import numpy as np
g=['G1','G2','G3','G4','G5']
m=[22, 30, 35, 35, 26]
w=[25, 32, 30, 35, 29]
X=np.arange(len(g))
plt.bar(X-0.2,m,width=0.4,label="men",color='green')
plt.bar(X+0.2,m,width=0.4,label="women",color='red')
plt.xticks(X,g)
plt.xlabel('person')
plt.xlabel('Scores')
plt.title('Scores by person')
plt.legend()
plt.show()
