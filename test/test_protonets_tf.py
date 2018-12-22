import numpy as np
from few_shot_learn.protonets import ProtoNetTF


def test_model():
    proto_net = ProtoNetTF(2, 2, 1)

    n_classes = 10
    n_examples_per_class = 2
    data_shape = (2, 2)
    data = np.random.randn(n_classes, n_examples_per_class, *data_shape)

    proto_net.train(data, 1, 1, 1, 1, 1)

    proto_net.test(data, 10, 1, 1, 1, 1)