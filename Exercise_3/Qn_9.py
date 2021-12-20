import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('medal.csv')
country_data = df["country"]
medal_data = df["gold_medal"]
plt.pie(medal_data, labels=country_data,autopct='%1.1f%%')
plt.show()
