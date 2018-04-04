import tensorflow as tf
import numpy as np

# In progress by Mel --> feel free to modify

# variables used:
# batch_size, embeddings_size
# hl_size = hidden layer hl_size
# z_size = (hidden layer + x) size


class Parameters(object):

    def __init__(self, hl_size, z_size):

        # Weights
        self.W_i = tf.Variable(tf.random_uniform((hl_size, z_size), -1, 1), name="W_i")
        self.W_f = tf.Variable(tf.random_uniform((hl_size, z_size), -1, 1), name="W_f")
        self.W_c = tf.Variable(tf.random_uniform((hl_size, z_size), -1, 1), name="W_c")
        self.W_o = tf.Variable(tf.random_uniform((hl_size, z_size), -1, 1), name="W_o")

        # Biases
        self.b_i = tf.Variable(tf.zeros((hl_size,)), name="b_i")
        self.b_f = tf.Variable(tf.zeros((hl_size,)), name="b_f")
        self.b_c = tf.Variable(tf.zeros((hl_size,)), name="b_c")
        self.b_o = tf.Variable(tf.zeros((hl_size,)), name="b_o")


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def tanh(x):
    return np.tanh(x)


class ForwardLSTM():
    def __init__(self, batch_size, embedding_dimensions, hl_size):
        self.x_in = tf.placeholder(tf.float32,
                                      shape=(batch_size, embedding_dimensions), name="x_input")

        self.hl_in = tf.placeholder(tf.float32,
                                    shape=(hl_size, hl_size), name="hl_in")

        self.C_in = tf.placeholder(tf.float32,
                                   shape=(batch_size, embedding_dimensions), name="C_in")

        self.z_in = np.row_stack(self.hl_in, self.x_input)

    def forward(self):
        #forget gate
        f_t = sigmoid(np.dot(self.W_f, self.z_in))
