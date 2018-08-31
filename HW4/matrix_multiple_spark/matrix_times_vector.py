from pyspark import SparkConf, SparkContext
import numpy as np

def matrix_vector(matrix_file,vector_file):
    conf = SparkConf()
    sc = SparkContext()

    A = sc.textFile(matrix_file).map(lambda l: [float(x) for x in l.split(",")])
    v = sc.textFile(vector_file).map(lambda l: l.split(","))

    A_1 = A.zipWithIndex()
    A_2 = A_1.map(lambda l: (l[1],[(i,l[0][i]) for i in range(len(l[0]))]))
    A_3 = A_2.flatMapValues(lambda l: l)
    A_4 = A_3.map(lambda l: (l[1][0],(l[0],l[1][1])))
    v_1 = v.flatMap(lambda l: [(i,float(l[i])) for i in range(len(l))])
    Av = A_4.join(v_1)
    Av_1 = Av.map(lambda l: (l[1][0][0],l[1][0][1]*l[1][1]))
    Av_2 = Av_1.reduceByKey(lambda l1,l2: l1+l2)

    return Av_2

if __name__=="__main__":
    print(matrix_vector('A.txt','B.txt').collect())