import os
import pandas as pd
import numpy as np

file_old = '../datasets/Melbourne_old.csv'
file_new = '../datasets/Melbourne.csv'

# read
data = pd.read_csv(file_old, sep=';', quotechar='"', skipinitialspace=True,
                   names=['price', 'landsize', 'building_area', 'lat', 'lng', 'bedrooms'])

# combine the area column
new_areas = []

for i in range(len(data['landsize'])):
    building_area = data['building_area'][i]
    landsize = data['landsize'][i]

    if str(building_area) == 'nan':
        new_areas.append(landsize)
    else:
        new_areas.append(building_area)


# add column and bring it in the right position with excel afterwards
data['area'] = pd.DataFrame(new_areas)

# delete old size area columns
del data['landsize']
del data['building_area']

# save again
data.to_csv(file_new, mode='w', sep=';', index=False)
