import numpy
import matplotlib.pyplot
from sklearn import svm
from sklearn.datasets import make_blobs
from Interfaces import IModel


class SupportVectorMachine(IModel.IModel):
    def __init__(self):
        self.model_type = 'svm'
        self.trained_model = False

        self.markers = ['o', "^", "s", "*", "D", "p", "X"]
        self.colors = ['b', 'c', 'k', 'g', 'm', 'r', 'y']

        self.training_data_X, self.training_data_y, self.test_data_X, self.test_data_y = self.create_blobs_dataset(3)

        self.classifier = svm.SVC(decision_function_shape='ovo')

        self.trainings_set_start = 0
        self.trainings_set_end = self.training_steps = 10

    def train(self, show_steps=False):
        self.trained_model = True

        if show_steps:
            if self.trainings_set_end <= 80:
                x = self.training_data_X[self.trainings_set_start:self.trainings_set_end, :]
                y = self.training_data_y[self.trainings_set_start:self.trainings_set_end]

                self.classifier.fit(x, y)

                self.trainings_set_start += self.training_steps
                self.trainings_set_end += self.training_steps
        else:
            if self.trainings_set_start < 80:
                self.classifier.fit(self.training_data_X[self.trainings_set_start:, :],
                                    self.training_data_y[self.trainings_set_start:])
            self.trainings_set_end = 101

    def test(self):
        result = self.classifier.predict(self.test_data_X)
        print("Predicted value = {}".format(result))
        print("expected values = {}".format(self.test_data_y))
        accuracy = numpy.sum(result == self.test_data_y) / len(self.test_data_y)
        print("Accuracy of the model is {}%".format(accuracy))

    def plot(self, axis):
        axis.cla()

        for i, value in enumerate(numpy.unique(self.training_data_y)):
            indices = numpy.where(self.training_data_y == value)
            new = self.training_data_X[indices]
            axis.scatter(new[:, 0], new[:, 1], marker=self.markers[i], c=self.colors[i])

        if self.trained_model:
            xlim = axis.get_xlim()
            ylim = axis.get_ylim()

            xx = numpy.linspace(xlim[0], xlim[1], 10)
            yy = numpy.linspace(ylim[0], ylim[1], 10)
            YY, XX = numpy.meshgrid(yy, xx)
            xy = numpy.vstack([XX.ravel(), YY.ravel()]).T
            Z = self.classifier.decision_function(xy)
            if len(Z.shape) > 1:
                for i in range(len(Z[0])):
                    hyperplane = Z[:, i].reshape(XX.shape)
                    axis.contour(XX, YY, hyperplane, colors=self.colors[i], levels=[0], alpha=0.5, linestyles=['-'])
            else:
                hyperplane = Z.reshape(XX.shape)
                axis.contour(XX, YY, hyperplane, colors=self.colors[0], levels=[0], alpha=0.5, linestyles=['-'])

        matplotlib.pyplot.show()

    def predict(self, features, axis=None):
        features = [[int(x)] for x in features]
        x = numpy.array(features).T
        result = self.classifier.predict(x)

        if axis is not None:
            axis.scatter(features[0][0], features[1][0], marker="X", c="red")

        return result

    def get_type(self):
        return "Support Vector Machine"

    def load_dataset(self):
        print("Loading dataset ...")
        dataset = numpy.genfromtxt("Resources/xyz", delimiter=',')
        dataset = numpy.delete(dataset, 0, axis=1)

        split_data = numpy.split(dataset, [80, 101])
        training_data = split_data[0][:, :-1]
        training_data_target = split_data[0][:, -1]
        test_data = split_data[1][:, :-1]
        test_data_target = split_data[1][:, -1]

        return training_data, training_data_target, test_data, test_data_target

    def create_blobs_dataset(self, centers):
        X, y = make_blobs(100, 2, centers=centers)

        split_data_x = numpy.split(X, [80, 100])
        split_data_y = numpy.split(y, [80, 100])
        training_data = split_data_x[0]
        training_data_target = split_data_y[0]
        test_data = split_data_x[1]
        test_data_target = split_data_y[1]

        return training_data, training_data_target, test_data, test_data_target
