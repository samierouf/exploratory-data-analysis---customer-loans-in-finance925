import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import statistics
from scipy.stats import norm   
import numpy as np
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot

class Plotter:

    def bar_chart_plot(self, index, values, xlabel='', ylabel='', title='', rotation=0, grid=bool, bar_width=0.8):
        plt.bar(index, values, width=bar_width)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=rotation)
        plt.grid(grid)
        plt.show()

    def hist_plotter(self, data, bins):
        data.hist(bins=bins, density=True)
        data.plot.density()

    def is_data_skew(self, data, column_name):
        skew = data[column_name].skew()
        return f'the skew of {column_name} is : {skew}'

    def qq_plotter(self, data, column_name):
        filtered_data = data[column_name].dropna()
        qqplot(filtered_data , scale=1 ,line='q', fit=True)
        pyplot.show()

    def box_plot(self, data, column_name):
        plt.title(f'{column_name}')
        sns.boxplot(data[column_name])
        plt.show()

    def scatter_plot(self, data):
        sns.scatterplot(data)
    
    def bar_chart(self, data):
        sns.barplot(data)
        
    


        