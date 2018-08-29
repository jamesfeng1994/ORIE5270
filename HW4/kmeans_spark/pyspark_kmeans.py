import sys
from pyspark import SparkConf, SparkContext
import numpy as np

def pyspark_kmeans(data_filename,seeds_filename):
    data = sc.textFile(data_filename).map(lambda l: l.split(" "))
    seeds = sc.textFile(seeds_filename).map(lambda l:l.split(" "))
    data = data.map(lambda l: np.array([float(x) for x in l]))
    seeds = np.array(seeds.map(lambda l: np.array([float (x) for x in l])).collect())
    iteration = 100
    
    for i in range(iteration):
        labeled_data = data.map(lambda l: (np.argmin([np.linalg.norm(l-s) for s in seeds]),(l,1)))
        seeds_1 = labeled_data.reduceByKey(lambda l1,l2: (l1[0]+l2[0],l1[1]+l2[1])).sortByKey()
        seeds_2 = seeds_1.map(lambda l: l[1][0]/l[1][1])
        seeds = np.array(seeds_2.collect())
    
    write_seeds(seeds)

def write_seeds(seeds):
    file = open("final_seeds.txt","w")
    for seed in seeds:
        line = ""
        for i in range(len(seed)-1):
            line += str(seed[i]) + " "
        line += "\n"
        file.write(line)
    file.close()

if __name__ == '__main__':
    sc = SparkContext()
    pyspark_kmeans("data.txt", "c1.txt")
    sc.stop()
