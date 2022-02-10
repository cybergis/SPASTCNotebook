#!/bin/bash
while IFS=, read -r WHOCARES GEOID NAME NAMELSAD; do
  echo "The GEOID is ${GEOID}, the name is ${NAMELSAD}"
  export GEOID=$GEOID
  export NAME=$NAME
  export NAMELSAD=$NAMELSAD
  python3 memory_estimate_continental.py
done < ../data/counties/ContinentalCounties/ContinentalUS.csv