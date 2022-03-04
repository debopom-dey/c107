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
            temp.append(float(row["Days Present"]))
            icecream_sales.append(float(row["Marks In Percentage"]))
    return {"x":temp,"y":icecream_sales}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Student Marks vs Days Present :",correlation[0,1])

def setup():
    path="Student Marks vs Days Present.csv"
    datasource=getDataSource(path)
    findCorrelation(datasource)

setup() 
