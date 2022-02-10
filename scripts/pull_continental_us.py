import geopandas as gpd
import itertools
import matplotlib.pyplot as plt
import multiprocessing
import os
import osmnx as ox
from shapely.validation import explain_validity
ox.config(use_cache=True, log_console=True)

FOLDER = "ContinentalUSPolygon-10kBuffer"
BUFFER = 10000
THREADS = 8

if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)
GRAPHML_FOLDER = os.path.join(FOLDER, "graphml")
PNG_FOLDER = os.path.join(FOLDER, "png")
if not os.path.exists(GRAPHML_FOLDER):
    os.mkdir(GRAPHML_FOLDER)
if not os.path.exists(PNG_FOLDER):
    os.mkdir(PNG_FOLDER)


def pull_place(polygon, geoid, GRAPHML_FOLDER, PNG_FOLDER):
    print("Pulling graph for {}".format(geoid))
    # check to see if exists:
    if os.path.exists("./{}/{}.graphml".format(GRAPHML_FOLDER, geoid)) and os.path.exists("./{}/{}.png".format(PNG_FOLDER, geoid)):
        print("{} already exists, skipping".format(geoid))
    else:
        try:
            G = ox.graph_from_polygon(polygon, network_type="drive")
            ox.save_graphml(G, "./{}/{}.graphml".format(GRAPHML_FOLDER, geoid))
            G_projected = ox.project_graph(G)
            del G
            fig, ax = ox.plot_graph(G_projected, show=False, save=True, filepath="./{}/{}.png".format(PNG_FOLDER, geoid))
            plt.close('all')
            del G_projected
        except Exception as e:
            print("Unable to pull {}".format(geoid))
            print(e)


def arg_unpacker(args):
    return pull_place(*args)


df = gpd.read_file("../data/geodata/counties/ContinentalCounties/ContinentalUS.shp")
df.drop_duplicates(inplace=True, subset="GEOID")
print(len(df))
df = df.to_crs("ESRI:102003")
df["geometry"] = df.geometry.buffer(BUFFER)
df = df.to_crs("EPSG:4326")
# geoids, polygons = list(df["AFFGEOID"]), list(df["geometry"])
geoids, polygons = [], []
for index, row in df.iterrows():
    geoids.append(df.at[index, "GEOID"])
    if not df.at[index, "geometry"].is_valid:
        print("{} polygon is not valid (per the shapely is_valid method), see explanation:\n{}".format(df.at[index, "GEOID"], explain_validity(df.at[index, "geometry"])))
        hull = df.at[index, "geometry"].convex_hull
        assert hull.is_valid
        polygons.append(hull)
    else:
        polygons.append(df.at[index, "geometry"])

with multiprocessing.Pool(processes=THREADS) as pool:
    pool.map(arg_unpacker, zip(polygons, geoids, itertools.repeat(GRAPHML_FOLDER), itertools.repeat(PNG_FOLDER)))
