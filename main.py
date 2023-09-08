import pandas as pd

###Descriptive Stats
def computation (data):
    average = data["Cooking_Skills"].mean()
    medium = data["Cooking_Skills"].median()
    #counts = data["Cooking_Skills"].mode()
    return (average,medium)


if __name__ == "__main__":
    data = {"Name": ["Simrun", "Rakeen", "Javier"], "Cooking_Skills": [1000, 300, 5000]}
# print(data)
df = pd.DataFrame.from_dict(data)
    
x  = computation (df)
print (x)
