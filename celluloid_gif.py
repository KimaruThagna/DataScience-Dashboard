import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from celluloid import Camera

#load irrigation dataset
irrigated_land = pd.read_csv('datasets/land_under_Irrigation.csv')
#print(irrigated_land.head())
# animation
fig = plt.figure(figsize=(80,40))
camera = Camera(fig) # bind camera object to matplotlib figure
for index, row in irrigated_land.iterrows():
    t = plt.bar(row['OBJECTID'], row['Total_Count'])
    plt.legend(t, [f'County {row["County"]}'])
    plt.title("Total acres of Land under Irrigation per County")
    camera.snap()

animation = camera.animate()
animation.save('celluloid_legends.gif', writer = 'imagemagick')