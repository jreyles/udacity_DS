import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
import csv

filename="turnstile_data_master_with_weather.csv"
weather_data = pd.read_csv(filename)


def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    plt.title('Residual Histogram')
    plt.xlabel('Residual')
    plt.ylabel('Frequency')
    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist()
    return plt

print plot_residuals(waether_data))