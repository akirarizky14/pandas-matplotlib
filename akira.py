import pandas as pd
import matplotlib.pyplot as mt

covid = pd.read_csv('data.csv',index_col=3, parse_dates=True)

print(covid['Active'])
mt.plot(covid['Total Cases'])
mt.plot(covid['Active'])
mt.show()


