import pandas as pd
import numpy as np
import seaborn.objects as sb
import matplotlib.pyplot as plt


#Loading Dataset
wdi = pd.read_csv(
    "https://media.githubusercontent.com/"
    "media/nickeubank/MIDS_Data/"
    "master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

#Taking the log of predictor variable(Gdp Per Capita) to determine relationship with outcome variable(Infant Mortality Rate)
wdi["Log GDP Per Capita"] = np.log(wdi["GDP per capita (constant 2010 US$)"])

#Visualizing the data representation of the relationship between the two variables. 
chart = (sb.Plot(wdi, x= "Log GDP Per Capita", y="Mortality rate, under-5 (per 1,000 live births)") 
.add(sb.Line(), sb.PolyFit(2)) 
.add(sb.Dot())
.label(title = "Analysis of Log Gdp Per Capita and Infant Mortality Rate")
)

#Display of the chart
plt.show(chart)

#Function created to understand the descriptive statistices for the dataset of WorldBank Indicators
def computation (dataframe):
    average = dataframe["Log GDP Per Capita"].mean()
    medium = dataframe["Log GDP Per Capita"].median()
    std_dev = dataframe["Log GDP Per Capita"].std()
    return (average,medium,std_dev)

#Calling the function
computation(wdi)










