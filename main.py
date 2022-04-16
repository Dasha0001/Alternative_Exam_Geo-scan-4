import numpy as np
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

from sklearn.datasets._samples_generator import make_blobs

centers = [[2, 2], [4, 5], [3, 10]]
X, _ = make_blobs(n_samples=500, centers=centers, cluster_std=1)
# X, _ = make_blobs(n_samples=500, centers=centers, cluster_std=1)
plt.scatter(X[:, 0], X[:, 1])

plt.show()
