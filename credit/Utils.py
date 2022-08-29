import numpy as np


class Utils:
    @staticmethod
    def same_shape(x, y):
        shape = np.maximum(x.shape, y.shape)
        x1 = np.zeros(shape)
        y1 = np.zeros(shape)
        x1[:x.shape[0], :x.shape[1]] = x
        y1[:y.shape[0], :y.shape[1]] = y

        return x1, y1

    @staticmethod
    def rounded_sum_arrays(x, y):
        x, y = Utils.same_shape(x, y)

        sum_yearly = np.add(x, y)
        return np.around(sum_yearly, 2)
