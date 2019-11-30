import fitting
import data
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn import neighbors, datasets

"""
"""

def make_probability_scatterplot(feature_1, feature_2):
    """
    6.3: Creates a scatter plot of diabetes data, displaying areas of predicted negative/positive result.

    Args:
        feature_1 (string): The first feature to plot by
        feature_2 (string): The second feature to plot by

    Returns:
        plt: the scatter plot
        float: the accuracy score on the training set
        float: the accuracy score on the validation set
    """
    trained_classifier, training_score, validation_score = fitting.fit('svc', include_features=[feature_1, feature_2])
    plt = data.create_scatter_plot(feature_1, feature_2);

    X = data.data_frame[[feature_1, feature_2]].values
    y = data.data_frame['diabetes'].values
    step = 0.5

    # Mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step),
                         np.arange(y_min, y_max, step))
    x_r = xx.ravel()
    y_r = yy.ravel()
    r = np.c_[x_r, y_r]
    Z = trained_classifier.predict(r)

    Z = Z.reshape(xx.shape)
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.coolwarm)

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    #plt.show(block=True)

    return plt, training_score, validation_score
