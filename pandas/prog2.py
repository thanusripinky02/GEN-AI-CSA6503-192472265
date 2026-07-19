import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df["Name"])