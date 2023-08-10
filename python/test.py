import pandas as pd

# 创建一个简单的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
})

for i, row in enumerate(df.itertuples(index=False)):
    print(f"Index: {i}, Row: {row}")