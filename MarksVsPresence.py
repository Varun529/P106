import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open("Student Marks vs Days Present.csv") as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="MarksInPercentage",y="DaysPresent")
        fig.show()

def getDataSource(data_path):
    Marks = []
    DaysPresent = []
    with open(data_path) as csv_file:
         csv_reader = csv.DictReader(csv_file)
         for row in csv_reader:
            Marks.append(float(row["MarksInPercentage"]))
            DaysPresent.append(float(row["DaysPresent"]))
    return {"x" : Marks, "y": DaysPresent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Student Marks vs Days Present ->",correlation[0,1])

def setup():
    data_path="Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()