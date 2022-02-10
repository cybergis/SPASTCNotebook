import os
import osmnx as ox
import psutil

geoid = os.environ["GEOID"]
name = os.environ["NAME"]
namelsad = os.environ["NAMELSAD"]
fgeoid = "0500000US{}".format(geoid)
MEM_CSV = "USContinental-MemoryUsage.csv"
GRAPHML_DIRECTORY = "./ContinentalUSPolygon-10kBuffer/graphml"
GRAPHML_FILE = os.path.join(GRAPHML_DIRECTORY, "{}.graphml".format(fgeoid))

if os.path.exists(GRAPHML_FILE):
    # print("Loading {}...".format(file))
    pre_load_mem_estimate = int(process.memory_info().rss) / 1000000000.0
    G = ox.load_graphml(GRAPHML_FILE)
    process = psutil.Process(os.getpid())
    memory_estimate = (int(process.memory_info().rss) / 1000000000.0) - pre_load_mem_estimate
    print("Estimated memory size: {:3.3f} GB".format(memory_estimate))
    if not os.path.exists(MEM_CSV):
        with open(MEM_CSV, "w") as csv_out:
            csv_out.write("FGEOID,GEOID,NAME,NAMELSAD,GEOID_FILE,Memory Usage (GB)\n")
            csv_out.flush()
    with open(MEM_CSV, "a") as csv_out:
        csv_out.write('{},{},{},{},"{}.graphml",{}\n'.format(fgeoid, geoid, name, namelsad, fgeoid, memory_estimate))
else:
    print("{} was not found".format(GRAPHML_FILE))
