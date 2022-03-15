# Building and Vegetation Height Model of São Paulo City

This dataset has buildings and vegetation heights from São Paulo city processed from LiDAR 3D data survey in 2017, available on [AWS Open Data](https://registry.opendata.aws/pmsp-lidar/).

## Dataset's Metadata

All tiff files represent spatial data with a spatial resolution of 50cm, and each pixel's value represents the height from the max value of Z-Axis to the DEM (Digital Earth Model) with 32bits.

## How are datasets organized?

There are files for the entire city purpose, and the three first letters represent the BHM (Building Height Model) and VHM (Vegetation Height Model). The folders represent squares of the city and contain single files with little squares inside. There is a file with the word 'merged' on int, which represents all content merged in a single file on each folder. The geometries of squares are available on [this project's repository on Github](https://github.com/AndaSampa/building-height-model) on the GIS folder as the methods to prepare and organize this dataset in appropriate folders and Python and Notebooks files.