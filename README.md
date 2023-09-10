# MiniProjectTemplate
[![.github/workflows/main.yml](https://github.com/simrunsharma/MiniProjectTemplate/actions/workflows/main.yml/badge.svg)](https://github.com/simrunsharma/MiniProjectTemplate/actions/workflows/main.yml)
![Visualization Example](https://user-images.githubusercontent.com/141798228/266807301-e455df10-7308-42a5-bb9d-d055e5e45f8f.jpg)

# Data Source
The dataset used in this analysis is retrieved from the World Development Indicators dataset for the year 2015. You can access the data from the following URL: World Development Indicators 2015 Dataset

# Code Overview
## 1. Loading the Dataset
The script loads the World Development Indicators dataset into a Pandas DataFrame.

## 2. Logarithm Transformation
It calculates the logarithm of the GDP per capita variable to analyze its relationship with the infant mortality rate.

## 3. Data Visualization
A scatterplot is created using Seaborn to visualize the relationship between log GDP per capita and infant mortality rate.

## 4. Descriptive Statistics
A function called computation is defined to compute descriptive statistics for the log GDP per capita variable, including the mean, median, and standard deviation.

## 5. Function Execution
The computation function is called with the DataFrame as input to calculate and display the statistics.

# Results
After executing the code, the following descriptive statistics were obtained for the log GDP per capita variable:

Mean: 8.6995653667 
Median: 8.7217498371 
Standard Deviation: 1.47
These statistics provide insights into the central tendency and spread of the log GDP per capita data, aiding in the understanding of its distribution.

# Conclusion
This script allows you to explore the relationship between log GDP per capita and infant mortality rate using World Development Indicators data and provides essential descriptive statistics for further analysis.

