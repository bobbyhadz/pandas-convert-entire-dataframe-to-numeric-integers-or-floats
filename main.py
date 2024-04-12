# Pandas: Convert entire DataFrame to numeric (int or float)

import pandas as pd


df = pd.DataFrame({
    'id': ['1', '2', '3', '4'],
    'experience': ['1', '1', '5', '7'],
    'salary': ['175.1', '180.2', '190.3', '205.4'],
})

print(df.dtypes)

df = df.apply(pd.to_numeric)

print('-' * 50)

print(df.dtypes)