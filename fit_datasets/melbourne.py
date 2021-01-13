import os
import pandas as pd
import numpy as np

file_old = '../datasets/Melbourne_old.csv'
file_new = '../datasets/Melbourne.csv'
file_descriptor = '../datasets/Melbourne.txt'

# read
data = pd.read_csv(file_old, sep=';', quotechar='"', skipinitialspace=True,
                   names=['price', 'landsize', 'building_area', 'lat', 'lng', 'bedrooms'])

# combine the area column
new_areas = []

for i in range(len(data['landsize'])):
    building_area = data['building_area'][i]
    landsize = data['landsize'][i]

    if str(building_area) != 'nan':
        new_areas.append(building_area)
    else:
        new_areas.append(landsize)

# add column and bring it in the right position with excel afterwards
data['area'] = pd.DataFrame(new_areas)

# delete old size area columns
del data['landsize']
del data['building_area']

# correct the lat / lng numbers (they have to many points in them)
# after the first point remove all other points
new_lats, new_lngs = [], []

for i in range(len(data['lat'])):
    lat = str(data['lat'][i])
    lng = str(data['lng'][i])

    if '.' in lat:
        nlat = lat.split('.')
        new_lats.append(nlat[0] + '.'.join(nlat[1:len(nlat)]))
    else:
        new_lats.append(lat)

    if '.' in lng:
        nlng = lng.split('.')
        new_lngs.append(nlng[0] + '.'.join(nlng[1:len(nlng)]))
    else:
        new_lngs.append(lng)

data['lat'] = pd.DataFrame(new_lats)
data['lng'] = pd.DataFrame(new_lngs)

# save again
data.to_csv(file_new, mode='w', sep=';', index=False)