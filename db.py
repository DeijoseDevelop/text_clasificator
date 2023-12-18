import pandas as pd
import polars as pl


df = pl.read_excel("test_data.xlsx")

data = []

for row in df.iter_rows(named=True):
    data.append({"text": row["wait for"], "label": "wait for"})
    data.append({"text": row["rent book"], "label": "rent book"})
    data.append({"text": row["use computer"], "label": "use computer"})
    data.append({"text": row["other"], "label": "other"})


# Split data into texts and labels
texts = [item['text'] for item in data]
labels = [item['label'] for item in data]