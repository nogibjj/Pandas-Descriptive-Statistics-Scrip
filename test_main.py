from main import computation

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def test_computation():
    wdi = pd.read_csv(
    "https://media.githubusercontent.com/"
    "media/nickeubank/MIDS_Data/"
    "master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

    result = computation(wdi)
    expected_mean = sum(wdi["Log GDP Per Capita"])/len(wdi["Log GDP Per Capita"])
    
    sort_wdi = sorted(wdi["Log GDP Per Capita"])
    n = len(sort_wdi)
    if n % 2 == 0:
      expected_median = (sort_wdi[n // 2-1] + sort_wdi[n //2]) / 2
    else:
      expected_median = sort_wdi[n//2]

    squared_diff_sum = sum((x - expected_mean)**2 for x in wdi["Log GDP Per Capita"])
    expected_standard_dev = (squared_diff_sum/len(wdi["Log GDP Per Capita"])) ** 0.5
  
    assert result == (expected_mean, expected_median, expected_standard_dev)

if __name__ == "__main__":
    pytest.main()
