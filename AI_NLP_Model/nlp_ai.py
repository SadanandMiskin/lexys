import pandas as pd
df= pd.read_csv("/content/Dateset_NLP.csv", names=["Text", "Labels"],header=None)
print(df.shape)
df.head(3)

import re
def Preprocess(text):
    # Remove extra white spaces, tabs, and line breaks
    text = re.sub('\s+', ' ', text)

    # Remove special characters and punctuation
    text = re.sub(r'[^\w\s]', '', text)

    return text