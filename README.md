# SCAMEL: A Novel Spatial Clustering Algorithm for Scalable SpatialAccessibility Analysis Under Memory Limits

![Accessibility for the Continental US](img/E2SFCA-OrRd.png)

**Repo Author:** Alexander Michels  
**Paper Authors:** Alexander Michels, Jeon-Young Kang, Jinwoo Park, and Shaowen Wang  
**Paper:** In preparation

SCAMEL is designed as a novel algorithm for paritioning points in space *together* with the spatial context of the points. It was specifically designed for enabling scalable and memory constrained travel-time catchment calculations for spatial accessibility analysis. This repository contains:

* `data` - the necessary data for SCAMEL and accessibility calculation. Due to file limits, we do not provide the OSM network data necessary for calculating travel-time. However, we do give pre-compute travel-time catchments for our hospital data set and...
* `scripts` - we provide the necessary scripts for pulling OSM networks with OSMnx for the entire Contiguous United States and calculating the memory usage of each county's road network!
* `notebooks` - notebooks for SCAMEL and accessibiilty at various spatial extents.

For more information about the data and scripts, see the READMEs in the respective directories.

## Notebooks

* Using SCAMEL:
  * Illinois: [notebooks/SCAMEL-Illinois.ipynb](notebooks/SCAMEL-Illinois.ipynb)
  * Midwest US: [notebooks/SCAMEL-Midwest.ipynb](notebooks/SCAMEL-Midwest.ipynb)
  * Contiguous US: [notebooks/SCAMEL-Contiguous.ipynb](notebooks/SCAMEL-Contiguous.ipynb)
* Calculating Enhanced Two-Step Floating Catchment Area (E2SFCA):
  * Illinois, Midwest, and Contiguous US: [notebooks/CalculateAccessibility.ipynb](notebooks/CalculateAccessibility.ipynb)


![Travel time catchments for our hospital dataset](img/TravelTimeCatchments.png)


*Image: Travel-time catchments for our hospital dataset*