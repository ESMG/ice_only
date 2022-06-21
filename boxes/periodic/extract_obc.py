#!/bin/env python
# Extract boundary conditions for the child domain from the output of
# the parent domain. Run this after extract_obc.bash.
import numpy as np
import netCDF4
import os
import sys
import subprocess
import numpy as np
from datetime import datetime

grd = netCDF4.Dataset('sea_ice_geometry.nc', "r")
prog = netCDF4.Dataset('10000101.daily.nc', "r")
east = netCDF4.Dataset('east.nc', 'a')
west = netCDF4.Dataset('west.nc', 'a')
north = netCDF4.Dataset('north.nc', 'a')
south = netCDF4.Dataset('south.nc', 'a')
spval = 1.e20

new = True
if new:
    west.createVariable('dvdx_segment_001', 'f8', ('time', 'yB', 'xB'), fill_value=spval)
    west.variables['dvdx_segment_001'].long_name = 'Part of vorticity.'
    west.variables['dvdx_segment_001'].units = '1/s'

    east.createVariable('dvdx_segment_002', 'f8', ('time', 'yB', 'xB'), fill_value=spval)
    east.variables['dvdx_segment_002'].long_name = 'Part of vorticity.'
    east.variables['dvdx_segment_002'].units = '1/s'

    south.createVariable('dudy_segment_004', 'f8', ('time', 'yB', 'xB'), fill_value=spval)
    south.variables['dudy_segment_004'].long_name = 'Layer thicknesses.'
    south.variables['dudy_segment_004'].units = '1/s'

    north.createVariable('dudy_segment_003', 'f8', ('time', 'yB', 'xB'), fill_value=spval)
    north.variables['dudy_segment_003'].long_name = 'Layer thicknesses.'
    north.variables['dudy_segment_003'].units = '1/s'

# Whole grid
v = prog.variables['vice'][:]
u = prog.variables['uice'][:]
hice = prog.variables['hice'][:]
aice = prog.variables['siconc'][:]
str_d = prog.variables['str_d'][:]
str_t = prog.variables['str_t'][:]
dx = grd.variables['dxBu'][:]
dy = grd.variables['dyBu'][:]

# Segment 1
dvdx = (v[:,5:16,5] - v[:,5:16,4]) / dx[5:16,5]
vseg = 0.5*(v[:,5:16,5] + v[:,5:16,4])
hseg = 0.5*(hice[:,5:15,5] + hice[:,5:15,4])
aseg = 0.5*(aice[:,5:15,5] + aice[:,5:15,4])
str_d_seg = 0.5*(str_d[:,5:15,5] + str_d[:,5:15,4])
str_t_seg = 0.5*(str_t[:,5:15,5] + str_t[:,5:15,4])

west.variables['dvdx_segment_001'][:] = dvdx
west.variables['vi_segment_001'][:] = vseg
west.variables['ai_segment_001'][:] = aseg
west.variables['hi_segment_001'][:] = hseg
west.variables['str_d_segment_001'][:] = str_d_seg
west.variables['str_t_segment_001'][:] = str_t_seg
west.close()

# Segment 2
dvdx = (v[:,5:15,15] - v[:,5:15,14]) / dx[5:16,15]
vseg = 0.5*(v[:,5:16,15] + v[:,5:16,14])
hseg = 0.5*(hice[:,5:15,15] + hice[:,5:15,14])
aseg = 0.5*(aice[:,5:15,15] + aice[:,5:15,14])
str_d_seg = 0.5*(str_d[:,5:15,15] + str_d[:,5:15,14])
str_t_seg = 0.5*(str_t[:,5:15,15] + str_t[:,5:15,14])

east.variables['dvdx_segment_002'][:] = dvdx
east.variables['vi_segment_002'][:] = vseg
east.variables['ai_segment_002'][:] = aseg
east.variables['hi_segment_002'][:] = hseg
east.variables['str_d_segment_002'][:] = str_d_seg
east.variables['str_t_segment_002'][:] = str_t_seg
east.close()

# Segment 3
dudy = (u[:,15,5:16] - u[:,14,5:16]) / dy[15,5:16]
useg = 0.5*(u[:,15,5:16] + u[:,14,5:16])
hseg = 0.5*(hice[:,15,5:15] + hice[:,14,5:15])
aseg = 0.5*(aice[:,15,5:15] + aice[:,14,5:15])
str_d_seg = 0.5*(str_d[:,15,5:15] + str_d[:,14,5:15])
str_t_seg = 0.5*(str_t[:,15,5:15] + str_t[:,14,5:15])

north.variables['dudy_segment_003'][:] = dudy
north.variables['ui_segment_003'][:] = useg
north.variables['ai_segment_003'][:] = aseg
north.variables['hi_segment_003'][:] = hseg
north.variables['str_d_segment_003'][:] = str_d_seg
north.variables['str_t_segment_003'][:] = str_t_seg
north.close()

# Segment 4
dudy = (u[:,5,5:16] - u[:,4,5:16]) / dy[5,5:16]
useg = 0.5*(u[:,5,5:16] + u[:,4,5:16])
hseg = 0.5*(hice[:,5,5:15] + hice[:,4,5:15])
aseg = 0.5*(aice[:,5,5:15] + aice[:,4,5:15])
str_d_seg = 0.5*(str_d[:,5,5:15] + str_d[:,4,5:15])
str_t_seg = 0.5*(str_t[:,5,5:15] + str_t[:,4,5:15])

south.variables['dudy_segment_004'][:] = dudy
south.variables['ui_segment_004'][:] = useg
south.variables['ai_segment_004'][:] = aseg
south.variables['hi_segment_004'][:] = hseg
south.variables['str_d_segment_004'][:] = str_d_seg
south.variables['str_t_segment_004'][:] = str_t_seg
south.close()
