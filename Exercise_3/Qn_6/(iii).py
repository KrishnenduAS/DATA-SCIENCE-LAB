import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 77, 6.7]
plt.bar(x, popularity,color=['black', 'red', 'green', 'blue', 'cyan','yellow'])
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.show()
