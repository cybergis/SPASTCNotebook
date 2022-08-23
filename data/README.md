# Data Information

* `geodata/counties` - county shapefiles for various spatial extents
* `hospitals` - Hospital data comes from the Homeland Infrastructure Foundation-Level Data (HIFLD). Download here: https://hifld-geoplatform.opendata.arcgis.com/datasets/geoplatform::hospitals-1/about
* `memory_df` - CSV file giving estimated memory usage for each county's road network, calculated using scripts in `scripts`
* `pop` - Population data comes from the Centers for Disease Control (CDC)/Agency for Toxic Substances and Disease Registry (ATSDR) Social Vulnerability Index (SVI). Download here: https://www.atsdr.cdc.gov/placeandhealth/svi/data_documentation_download.html
* `regions` - holds pre-computed travel-time catchments for our hospital dataset using the SCAMEL method

A full breakdown of the data directory:

```
.
├── geodata
│   └── counties
│       ├── ContinentalCounties
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
└── regions
    ├── Continental
    │   ├── ContClustering.png
    │   ├── resource_catchments_1200distance.shp
    │   ├── resource_catchments_1800distance.shp
    │   └── resource_catchments_600distance.shp
    ├── Illinois
    │   ├── ILClustering.png
    │   ├── resource_catchments_1200distance.geojson
    │   ├── resource_catchments_1800distance.geojson
    │   └── resource_catchments_600distance.geojson
    └── Midwest
        ├── MidwestClustering.png
        ├── resource_catchments_1200distance.geojson
        ├── resource_catchments_1800distance.geojson
        └── resource_catchments_600distance.geojson

18 directories, 68 files
```