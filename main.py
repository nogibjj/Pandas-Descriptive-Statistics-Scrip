import pandas as pd

data = {"Name": ["Simrun", "Rakeen", "Javier"], "Cooking_Skills": [1000, 300, 5000]}
print(data)
df = pd.DataFrame(data.items(), columns=["Name", "Cooking_Skills"])
df.describe()
exit()
# Descriptive Stats
average = df["Cooking_Skills"].mean()
medium = df["Cooking_Skills"].median()
counts = df["Cooking_Skills"].value_counts()

if __name__ == "__main__":
    print(average)
    print(medium)
    print(counts)
