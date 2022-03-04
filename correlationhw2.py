from statistics import correlation
import plotly.express as px
import csv
import numpy as np

def getDataSource(path):
    temp=[]
    icecream_sales=[]
    with open(path) as f:
        df = csv.DictReader(f)
        for row in df:
            temp.append(float(row["Coffee"]))
            icecream_sales.append(float(row["sleep"]))
    return {"x":temp,"y":icecream_sales}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Coffee vs Sleep :",correlation[0,1])

def setup():
    path="cups of coffee vs hours of sleep.csv"
    datasource=getDataSource(path)
    findCorrelation(datasource)

setup() 
