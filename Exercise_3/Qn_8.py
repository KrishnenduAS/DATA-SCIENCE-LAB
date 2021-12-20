import matplotlib.pyplot as plt
import numpy as np
y=np.array([22.2, 17.6, 8.8, 8, 77, 6.7])
mylabel=np.array(['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'])
plt.pie(y,labels=mylabel,autopct='%1.1f%%')
plt.show()
