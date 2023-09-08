from main import computation
import pandas as pd

def test_computation():
    data = {"Name": ["Simrun", "Rakeen", "Javier"], "Cooking_Skills": [1000, 300, 5000]}
    # print(data)
    df = pd.DataFrame.from_dict(data)
        
    
    assert computation(df) == (2100.0,1000.0)
