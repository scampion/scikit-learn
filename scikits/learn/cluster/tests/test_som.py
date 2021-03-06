"""
Testing for SOM

"""
import numpy as np
from numpy.testing import assert_equal

from ..som_ import SelfOrganizingMap
from .common import generate_clustered_data

n_clusters = 4
n_features = 2
X = generate_clustered_data(n_clusters=n_clusters, n_features=2, std=.1)


def test_som():
    np.random.seed(1)
    som = SelfOrganizingMap(size=2, n_iterations=10, learning_rate=1)
    som.fit(X)
    labels = som.labels_

    assert_equal(np.unique(labels).shape[0], 4)
    assert_equal(np.unique(labels[:20]).shape[0], 1)
    assert_equal(np.unique(labels[20:40]).shape[0], 1)
    assert_equal(np.unique(labels[40:60]).shape[0], 1)
    assert_equal(np.unique(labels[60:]).shape[0], 1)

def test_som_init_matrix():
    np.random.seed(1)
    random_ind = np.random.randint(0, X.shape[0], size=n_clusters)
    init_map = X[random_ind].reshape(2,2,n_features)

    som = SelfOrganizingMap(size=init_map, init='matrix',
                            n_iterations=2000, learning_rate=0.1)

    som.fit(X)
    labels = som.labels_
    assert_equal(np.unique(labels).shape[0], 4)
    assert_equal(np.unique(labels[:20]).shape[0], 1)
    assert_equal(np.unique(labels[20:40]).shape[0], 1)
    assert_equal(np.unique(labels[40:60]).shape[0], 1)
    assert_equal(np.unique(labels[60:]).shape[0], 1)
