import plotly.express as py
import csv
import numpy as np

def get_data_source(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for i in reader:
            coffee.append(float(i["Coffee in ml"]))
            sleep.append(float(i["sleep in hours"]))
        
    return{"x": coffee, "y": sleep}

def find_corelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    # print("correlation between temperature and ice-cream-sales", correlation[0,1])
    print("correlation between Amount of coffee and Sleep", correlation[0,1])


def setup():
    data_path = "Coffee_Sleep.csv"
    data_source = get_data_source(data_path)
    plotfigure(data_path)
    find_corelation(data_source)

def plotfigure(data_path):
    with open(data_path) as csvfile:
        reader = csv.DictReader(csvfile)
        fig = py.scatter(reader, x="Coffee in ml", y="sleep in hours")
        fig.show()

setup()

input ("You Can Quit Now")