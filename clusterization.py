import random

import numpy as np
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt
from matplotlib import style

from mpl_toolkits import mplot3d

style.use("ggplot")

k = 10
array = []
for i in range(100):
    array.append([0] * 2)

for i in range(100):
    for j in range(2):
        array[i][j] = random.randint(0, 100)
print(array)


def data_distribution(array, cluster):
    cluster_content = [[] for i in range(k)]
    n = 5
    dim = 2
    for i in range(n):
        min_distance = float('inf')
        situable_cluster = -1
        for j in range(k):
            distance = 0
            for q in range(dim):
                distance += (array[i][q] - cluster[j][q]) ** 2

            distance = distance ** (1 / 2)
            if distance < min_distance:
                min_distance = distance
                situable_cluster = j

        cluster_content[situable_cluster].append(array[i])

    return cluster_content


def clusterization(array, k):
    n = 100


dim: int = 2

cluster = [[0 for i in range(dim)] for q in range(k)]
cluster_content = [[] for i in range(k)]

for i in range(dim):
    for q in range(k):
        cluster[q][i] = random.randint(0, 100)

cluster_content = data_distribution(array, cluster)


def cluster_update(cluster, cluster_content, dim):
    k = len(cluster)
    for i in range(k):  # по i кластерам
        for q in range(dim):  # по q параметрам
            updated_parameter = 0
            for j in range(len(cluster_content[i])):
                updated_parameter += cluster_content[i][j][q]
            if len(cluster_content[i]) != 0:
                updated_parameter = updated_parameter / len(cluster_content[i])
            cluster[i][q] = updated_parameter
    return cluster


def visualisation_2d(cluster_content):
    k = len(cluster_content)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")

    for i in range(k):
        x_coordinates = []
        y_coordinates = []
        for q in range(len(cluster_content[i])):
            x_coordinates.append(cluster_content[i][q][0])
            y_coordinates.append(cluster_content[i][q][1])
        plt.scatter(x_coordinates, y_coordinates)
    plt.show()


visualisation_2d(cluster_content)
