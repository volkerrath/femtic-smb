# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import numpy as np
import rasterio
import rasterio.plot
import  utm
import elevation
import matplotlib.pyplot as plt




download_dem = False

# filename_dem = '/home/sbyrd/Desktop/srtm/Annecy_NASADEM.tif' # good one
filename_dem = '/home/sbyrd/Desktop/srtm/Annecy_dem.tif' 
filename_dem_utm_xyz = filename_dem.replace('.tif', '_utm_xyz.dat') 


file_out= open(filename_dem_utm_xyz, 'w')

if download_dem:
    left=5.6
    right=6.6
    bottom=45.3
    top=46.3
    carte = elevation.clip(bounds=(left, bottom, right, top), output = filename_dem)
    ## clean up stale temporary files and fix the cache in the event of a server error
    elevation.clean()
 

carte = rasterio.open(filename_dem)
z0 = carte.read()[0]
carte.crs
carte.bounds
rasterio.plot.show(carte)

left = np.around(carte.bounds[0], decimals=3) 
bottom = np.around(carte.bounds[1], decimals=3)
right = np.around(carte.bounds[2], decimals=3)
top = np.around(carte.bounds[3], decimals=3)

n_lat = carte.shape[0]
n_lon = carte.shape[1]
inc_lat = (top-bottom)/(n_lat)
inc_lon = (right-left)/(n_lon)

lat_cell = np.arange(bottom, top, inc_lat, dtype=float)
lon_cell = np.arange(left, right, inc_lon, dtype=float)


utm_coord = utm.from_latlon(lat_cell , lon_cell)
utmn = utm_coord[0]
utme = utm_coord[1]
utmn_grid, utme_grid = np.meshgrid(utmn, utme)

nord = np.around(1e-3*utmn_grid.ravel(), decimals=3)
east = np.around(1e-3*utme_grid.ravel(), decimals=3)
z = np.around(1e-3*z0.ravel(), decimals=3)
    
dem = np.vstack([nord, east, -z])


for ipx in np.arange(np.shape(dem)[1]):
    line = '   '.join([
        str(dem[0,ipx]), 
        str(dem[1,ipx]), 
        str(dem[2,ipx]),
        '\n'
        ])
    
    file_out.write(line)    
 
# img = dem[2,:].reshape((3600, 3600))
# plt.imshow(img)








