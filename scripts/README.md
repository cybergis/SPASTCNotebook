# Scripts

Scripts for pull OSM networks and estimating their memory usage.

**NOTE:** You will have to change paths to run these scripts. This is done intentionally
because these scripts can be memory, CPU, and I/O intensive. Please read the scripts
carefully.

## Pulling the Network

* `pull_continental_us.py` - pulls the OSMnx network for the Continental United States by county with a buffer given a shapefile of the countys

## Estimating Memory Usage

* `memory_estimate_continental.py` - estimates the memory usage of a piece of network in memory by measuring the memory usage of process
* `run_memory_estimate.sh` - a Bash script to read counties from a CSV file and call `memory_estimate_continental.py`.
