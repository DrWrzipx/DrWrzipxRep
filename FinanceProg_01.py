import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

style.use('ggplot')

#start = dt.datetime(2015, 1, 1)
#end = dt.datetime.now()
#df = web.DataReader("TWTR", 'morningstar', start, end)
#df.reset_index(inplace=True)
#df.set_index("Date", inplace=True)
#df = df.drop("Symbol", axis=1)

# print(df.tail(5))  # df.tail(5) df.head(5)

#df.to_csv('twir.cvs')

df = pd.read_csv('twir.cvs', parse_dates=True, index_col=0)
#print(df.head()
df[['Open', 'Close']].plot()
plt.show()