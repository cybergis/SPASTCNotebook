# Data Information

* `geodata/counties` - county shapefiles for various spatial extents
* `hospitals` - Hospital data comes from the Homeland Infrastructure Foundation-Level Data (HIFLD). Download here: https://hifld-geoplatform.opendata.arcgis.com/datasets/geoplatform::hospitals-1/about
* `memory_df` - CSV file giving estimated memory usage for each county's road network, calculated using scripts in `scripts`
* `pop` - Population data comes from the Centers for Disease Control (CDC)/Agency for Toxic Substances and Disease Registry (ATSDR) Social Vulnerability Index (SVI). Download here: https://www.atsdr.cdc.gov/placeandhealth/svi/data_documentation_download.html
* `regions` - holds pre-computed travel-time catchments for our hospital dataset using the SPACTS method
* `runtime` - data on the runtimes from benchmarking the code on Expanse

A full breakdown of the data directory:

```
.
├── geodata
│   └── counties
│       ├── ConterminousCounties
│       │   ├── ContinentalUS.cpg
│       │   ├── ContinentalUS.csv
│       │   ├── ContinentalUS.dbf
│       │   ├── ContinentalUS.prj
│       │   ├── ContinentalUS.shp
│       │   └── ContinentalUS.shx
│       ├── ILCounties
│       │   ├── ILCountyShapefile.cpg
│       │   ├── ILCountyShapefile.dbf
│       │   ├── ILCountyShapefile.prj
│       │   ├── ILCountyShapefile.shp
│       │   └── ILCountyShapefile.shx
│       └── MidwestCounties
│           ├── MidwestCounties.cpg
│           ├── MidwestCounties.dbf
│           ├── MidwestCounties.geojson
│           ├── MidwestCounties.prj
│           ├── MidwestCounties.shp
│           └── MidwestCounties.shx
├── hospitals
│   ├── continental
│   │   ├── ContinentalHospitals.cpg
│   │   ├── ContinentalHospitals.dbf
│   │   ├── ContinentalHospitals.prj
│   │   ├── ContinentalHospitals.shp
│   │   └── ContinentalHospitals.shx
│   ├── Hospitals.cpg
│   ├── Hospitals.dbf
│   ├── Hospitals.prj
│   ├── Hospitals.shp
│   ├── Hospitals.shx
│   ├── Hospitals.xml
│   ├── illinois
│   │   ├── IllinoisHospitals.cpg
│   │   ├── IllinoisHospitals.dbf
│   │   ├── IllinoisHospitals.geojson
│   │   ├── IllinoisHospitals.prj
│   │   ├── IllinoisHospitals.shp
│   │   └── IllinoisHospitals.shx
│   └── midwest
│       ├── MidwestHospitals.cpg
│       ├── MidwestHospitals.dbf
│       ├── MidwestHospitals.prj
│       ├── MidwestHospitals.shp
│       └── MidwestHospitals.shx
├── memory_df
│   └── USCounty-MemoryUsage.csv
├── pop
│   ├── continental
│   │   ├── Continental_SVI_CT.cpg
│   │   ├── Continental_SVI_CT.dbf
│   │   ├── Continental_SVI_CT.prj
│   │   ├── Continental_SVI_CT.shp
│   │   └── Continental_SVI_CT.shx
│   ├── illinois
│   │   ├── SVI2018_IL_tract.cpg
│   │   ├── SVI2018_IL_tract.dbf
│   │   ├── SVI2018_IL_tract.prj
│   │   ├── SVI2018_IL_tract.shp
│   │   └── SVI2018_IL_tract.shx
│   └── midwest
│       ├── Midwest_SVI_CT.cpg
│       ├── Midwest_SVI_CT.dbf
│       ├── Midwest_SVI_CT.prj
│       ├── Midwest_SVI_CT.shp
│       └── Midwest_SVI_CT.shx
├── README.md
├── regions
│   ├── Conterminous
│   │   ├── catchments
│   │   │   ├── 0000000117
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0000401608
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0000822630
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0001422554
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0001913856
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0002061081
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0002328106
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0003435150
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0003566801
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0003906250
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0004765560
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0004965041
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0005021237
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0005189410
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0005587049
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0005784060
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0005998020
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0006540359
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0006728379
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0007327565
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0007446526
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0008130701
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0008390804
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0009436507
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0010685132
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0013474079
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0014408854
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0015037804
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0015319601
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0015548183
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0015654985
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0016045331
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0016738019
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0016760033
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0017470444
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0025133029
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0026691342
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0039595231
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0042079072
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0050378957
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0076777520
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0082676234
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   └── 0108408096
│   │   │       ├── resource_catchments_1200distance.geojson
│   │   │       ├── resource_catchments_1800distance.geojson
│   │   │       └── resource_catchments_600distance.geojson
│   │   ├── ContClustering.jpg
│   │   ├── ContClustering-NaivevsSPACTS-16gb.jpg
│   │   ├── ContinentalCatchments.jpg
│   │   ├── E2SFCA-OrRd.jpg
│   │   ├── E2SFCA-RdBu.jpg
│   │   ├── resource_catchments_1200distance.geojson
│   │   ├── resource_catchments_1800distance.geojson
│   │   └── resource_catchments_600distance.geojson
│   ├── Illinois
│   │   ├── catchments
│   │   │   ├── 0001261364
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0001360504
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0003561108
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0005060450
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0007961701
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   ├── 0012460115
│   │   │   │   ├── resource_catchments_1200distance.geojson
│   │   │   │   ├── resource_catchments_1800distance.geojson
│   │   │   │   └── resource_catchments_600distance.geojson
│   │   │   └── 0100962263
│   │   │       ├── resource_catchments_1200distance.geojson
│   │   │       ├── resource_catchments_1800distance.geojson
│   │   │       └── resource_catchments_600distance.geojson
│   │   ├── E2SFCA-OrRd.jpg
│   │   ├── E2SFCA-RdBu.jpg
│   │   ├── ILClustering.jpg
│   │   ├── resource_catchments_1200distance.geojson
│   │   ├── resource_catchments_1800distance.geojson
│   │   └── resource_catchments_600distance.geojson
│   └── Midwest
│       ├── catchments
│       │   ├── 0000000072
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0000000094
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0001261364
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0001261856
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0001360504
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0001460123
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0001746904
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0001762801
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0003155021
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0003267526
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0003368788
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0003749202
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0003848617
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0004863090
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0004965041
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0005047804
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0005255371
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0005555066
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0005965548
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0006243606
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0006540359
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0006746151
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0007446526
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0007455720
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0007844857
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0008560098
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0009960048
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0010446750
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0010560451
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0010653105
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0011261354
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0011353548
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0011450801
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0012760169
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0013843338
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0013944622
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0014348118
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0014453188
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0015354449
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0015548183
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0015654985
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0016045331
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0016760033
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0017351250
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0018162286
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0100460548
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   ├── 0102640475
│       │   │   ├── resource_catchments_1200distance.geojson
│       │   │   ├── resource_catchments_1800distance.geojson
│       │   │   └── resource_catchments_600distance.geojson
│       │   └── 0157366536
│       │       ├── resource_catchments_1200distance.geojson
│       │       ├── resource_catchments_1800distance.geojson
│       │       └── resource_catchments_600distance.geojson
│       ├── E2SFCA-OrRd.jpg
│       ├── E2SFCA-RdBu.jpg
│       ├── MidwestClustering.jpg
│       ├── resource_catchments_1200distance.geojson
│       ├── resource_catchments_1800distance.geojson
│       └── resource_catchments_600distance.geojson
└── runtime
    ├── Par_Timings-20G-117ad41632d01ee965fdb02bd2738160.csv
    ├── Par_Timings-20G-147b9419cec9dcaaf348cf491ee24d14.csv
    ├── Par_Timings-20G-178c42109401615102cf239d0742118f.csv
    ├── Par_Timings-20G-1ca2a42e6a2a1433c4892679ed9e35ec.csv
    ├── Par_Timings-20G-55f3189e17e9718b9003ffdf4f4e7f85.csv
    ├── Par_Timings-20G-8682adaafb99f6437050bbc45f26835b.csv
    ├── Par_Timings-20G-dae234b41c9becfa9dc61be4fa9a098f.csv
    ├── Par_Timings-20G-e759f5a6bc3da9fd88c359baf13bbd91.csv
    ├── Par_Timings-20G-ec01fe24c7d23f9adba8368a84a07d08.csv
    ├── Par_Timings-20G-f3901441cf7e0fad2390ada3370c7c0c.csv
    ├── Par_Timings-26G-299142cdab84c4e6e22618ddd37b3f9c.csv
    ├── Par_Timings-26G-411ba9013410d409c11d9384e367bd05.csv
    ├── Par_Timings-26G-5dd5239e0d651daf95fd0759b36ae8df.csv
    ├── Par_Timings-26G-75aa50e3e61ddcb8bf5a98d5c590b6dc.csv
    ├── Par_Timings-26G-9b2145c52c00a283c24344e51797817d.csv
    ├── Par_Timings-26G-9f5c4abb9bb150871ad9b79564ebf680.csv
    ├── Par_Timings-26G-a4ab1cad4a1d37457d650164af4b2ebe.csv
    ├── Par_Timings-26G-b08fed1e2364a9fea3009d0f1c271f4f.csv
    ├── Par_Timings-26G-dc85d3a87e2442525a6167c1a0ae6753.csv
    ├── Par_Timings-26G-f0ebc1dda6587b8071e3edc7a1c23c0f.csv
    ├── Par_Timings-32G-061e17faef83eaefd8d441f9681c19b3.csv
    ├── Par_Timings-32G-0c185ad1162f26f93a75032c336a7f42.csv
    ├── Par_Timings-32G-1509d39824b22a1993ed277d8bf5b726.csv
    ├── Par_Timings-32G-34c5e43670f512d70125250d2c7e9bbe.csv
    ├── Par_Timings-32G-37014b803a4f87794a51148117f645f5.csv
    ├── Par_Timings-32G-802ddabef17804d755c43ddf3507f284.csv
    ├── Par_Timings-32G-8c2735b9d6cbf1dd9da89c1c0e237675.csv
    ├── Par_Timings-32G-9197e80a9c1f59d8f54e3e774ba795e5.csv
    ├── Par_Timings-32G-d355f4f97f522033eb41cc0fc6f24601.csv
    ├── Par_Timings-32G-f83e4489f99208d818fa911ca4d827ca.csv
    ├── Par_Timings-40G-0af0b2fe2a91d524748cddec48a92fbf.csv
    ├── Par_Timings-40G-335bad85d8e0d6f65e1da93a2e20a988.csv
    ├── Par_Timings-40G-364957605653a0ae8bb8ace0f3705351.csv
    ├── Par_Timings-40G-5967217086834606d59e85e46bf22cdc.csv
    ├── Par_Timings-40G-6a057da904518fb30aae26c5dae8e1dd.csv
    ├── Par_Timings-40G-92b050f0598f29b87353b05cdf8c6e28.csv
    ├── Par_Timings-40G-b5655ab548351683bd9bf0256ce69353.csv
    ├── Par_Timings-40G-ccdbbf8a15e3e96585f26560a198b652.csv
    ├── Par_Timings-40G-e16378c3afd250de1b4b31dcb8b56195.csv
    ├── Par_Timings-40G-f98b521edbcd9463a9a5110a2b9e0858.csv
    ├── Par_Timings-48G-223067656a82ca32bd78fd7e6652d6c0.csv
    ├── Par_Timings-48G-24f8a35e1abf0d072cd0c5ae34b48237.csv
    ├── Par_Timings-48G-333cbc1d2165fdd4bd3e5b669dfacb1e.csv
    ├── Par_Timings-48G-349c9d0b49932f23ea1c8424ad3221f1.csv
    ├── Par_Timings-48G-3979bfc2d60ddcf351be5f058f7111d4.csv
    ├── Par_Timings-48G-6c6503954ecda05641cb871d6328280d.csv
    ├── Par_Timings-48G-702bacac9373d5830fdf38a92d7334ac.csv
    ├── Par_Timings-48G-9cec662b5efe77ab30baabe2e2871e87.csv
    ├── Par_Timings-48G-9d1c01bd08b5335adb515b3f11f1dd5f.csv
    ├── Par_Timings-48G-f2ee56468b83f33bf203a0305a6418cc.csv
    ├── Par_Timings-56G-2124b06ab8ca006d80accfa0279ace57.csv
    ├── Par_Timings-56G-3ebe49eaa2b31984fcbaa75522d92f0b.csv
    ├── Par_Timings-56G-50bead534c2fc9f751bafc9ac5dd44f1.csv
    ├── Par_Timings-56G-5e8ba66244f76d685b952371a4d7041f.csv
    ├── Par_Timings-56G-7936c924ea740da83e2e5fd07bff6ae4.csv
    ├── Par_Timings-56G-81c8923e98320d5f2fe42b0b593f316f.csv
    ├── Par_Timings-56G-9cc2db6826c5ede3df999eed8a27d518.csv
    ├── Par_Timings-56G-a894a1b3dd551ead43a8dc7e25caf1b8.csv
    ├── Par_Timings-56G-b5c16dbdb96e9a35e284e4cb94964c76.csv
    ├── Par_Timings-56G-e372dde864dfedd75466aff63e451c8b.csv
    ├── Par_Timings-64G-068e29337ffd24ad9476e91a40855c43.csv
    ├── Par_Timings-64G-10643319c237be189a35a1c5aeed91e3.csv
    ├── Par_Timings-64G-2ed3f1dbdda6413f0918a0589bc63710.csv
    ├── Par_Timings-64G-4b5f63d6a3bfbb49f8919e2eac8d7a56.csv
    ├── Par_Timings-64G-56c5a4bbd52f7446f0c222e76c7de8aa.csv
    ├── Par_Timings-64G-56e490ebafe5c5a40fcab7fe5cb01e2a.csv
    ├── Par_Timings-64G-7af25f5f3b2649935fad38f68ff2c019.csv
    ├── Par_Timings-64G-801924316b79fba7f9f543b09ea893c3.csv
    ├── Par_Timings-64G-80282f4059d1e937c4b2a34132bfebd3.csv
    ├── Par_Timings-64G-8cbc5f67c4dbd3c91cf1165af105cd68.csv
    ├── Par_Timings-72G-1df498a3ff2946e1688bdf0ce9a20df1.csv
    ├── Par_Timings-72G-3ba4a79f162364d37968a8c0d73227a4.csv
    ├── Par_Timings-72G-5dedb31f413c2c427b8cb957a02d34bc.csv
    ├── Par_Timings-72G-746044c3ee99b6a68940eac3e90a0b47.csv
    ├── Par_Timings-72G-86b4b397e942ae9d66d3c2be08c5e7f0.csv
    ├── Par_Timings-72G-8ba343953409a8999bfa30170fc86b2f.csv
    ├── Par_Timings-72G-97d5eb48550397025e7b699513f00f86.csv
    ├── Par_Timings-72G-c8f963be05ed8b11e878d40f7436181e.csv
    ├── Par_Timings-72G-ead47e63a3706e3040412df1f2078dc2.csv
    ├── Par_Timings-72G-f332b6d7ec714050ae60dba706157375.csv
    ├── Par_Timings-NM-1fe849c878d6088ca831e8b4be1098cd.csv
    ├── Par_Timings-NM-23fa5c45ff1a794c189a061a0d41cdb3.csv
    ├── Par_Timings-NM-273cf21011c3b473350a909f7ee0deb9.csv
    ├── Par_Timings-NM-4a3a4f0bb0ee1f1fb95c317d6d7be561.csv
    ├── Par_Timings-NM-6a2666d93098054417de38f9d3e7e33e.csv
    ├── Par_Timings-NM-707aabbc06410454121831e436a994e7.csv
    ├── Par_Timings-NM-74821fbb764edd581ff552d441f730dd.csv
    ├── Par_Timings-NM-7acbc3359544545a90f3792a6023d64d.csv
    ├── Par_Timings-NM-7c4207c693bfe603d65820fdbf21e010.csv
    └── Par_Timings-NM-d0dd95d0f36d4be0276c0f8ee9727045.csv

120 directories, 460 files
```