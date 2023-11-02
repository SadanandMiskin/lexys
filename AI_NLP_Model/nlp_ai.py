import pandas as pd
df= pd.read_csv("/content/Dateset_NLP.csv", names=["Text", "Labels"],header=None)
print(df.shape)
df.head(3)