import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from celluloid import Camera

#load irrigation dataset
irrigated_land = pd.read_csv('datasets/land_under_Irrigation.csv')
print(irrigated_land.head())