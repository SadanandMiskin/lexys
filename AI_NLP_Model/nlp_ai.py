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

from tranformers import BertTokenizer, BertForSequenceClassification, BertForMaskedLM

class LegalDocumentDataset(Dataset):
    def _init_(self, texts, labels, tokenizer, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def _len_(self):
        return len(self.texts)

    def _getitem_(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoding = self.tokenizer(
            text, padding='max_length', truncation=True, max_length=self.max_length, return_tensors='pt'
        )
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': label
        }