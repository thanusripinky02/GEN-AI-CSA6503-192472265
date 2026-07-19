import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [85, 90, 88]
}
df = pd.DataFrame(data)
# Add a new column
df["Result"] = ["Pass", "Pass", "Pass"]
print(df)