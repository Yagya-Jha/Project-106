import plotly.express as py
import csv
import numpy as np

def get_data_source(data_path):
    marks = []
    days = []
    with open(data_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for i in reader:
            marks.append(float(i["Marks In Percentage"]))
            days.append(float(i["Days Present"]))
        
    return{"x": marks, "y": days}

def find_corelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation of marks and days present of students:", correlation[0,1])


def setup():
    data_path = "Marks_Days.csv"
    data_source = get_data_source(data_path)
    plotfigure(data_path)
    find_corelation(data_source)

def plotfigure(data_path):
    with open(data_path) as csvfile:
        reader = csv.DictReader(csvfile)
        fig = py.scatter(reader, x="Marks In Percentage", y="Days Present")
        fig.show()

setup()

input ("You Can Quit Now")