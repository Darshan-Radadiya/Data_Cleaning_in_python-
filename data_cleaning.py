import pandas as pd
import numpy as np

df = pd.read_csv("weather.numeric.csv")
df.isna()

# 1. With global constant unkown
global c
c = 'unknown'
print("FILLING MISSING VALUE WITH GLOBAL CONSTANT UNKNOWN \n")
a = df.fillna(c)
print(a)

# 2. with mean
nume = df[['temprature','humidity']]
cate = df[['outlook','play','windy']]
b = nume.fillna(np.mean(nume))
print('FILLING MISSING VALUE WITH MEAN...\n\n',b)

# 3. with median
c = nume.fillna(np.nanmedian(nume))
print(“Fill with median..\n\n”c)
con = pd.concat([a['outlook'], b, a['windy'], a['play']], axis=1)
print(con)

# 4. normalization

  #4.1 Min-Max
  min_max = ( (b - (b.min()))/( (b.max()) - (b.min()) ) )
  print("Min-Max Normalization...\n\n",min_max)

  # 4.2 z-score
  z_score = ((b - np.mean(b))/np.std(b))
  print("Z-score normalization..\n\n",z_score)

  # 4.3 decimal scalling
  deci = b/(100)
  print("Decimal scalling...\n\n",deci)
