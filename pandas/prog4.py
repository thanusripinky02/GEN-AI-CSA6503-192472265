import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

result = df[df["Marks"] > 85]

print(result)