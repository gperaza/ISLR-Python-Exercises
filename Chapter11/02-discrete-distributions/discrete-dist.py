from random import random
import matplotlib.pyplot as plt
from collections import Counter


def plot_prob_mass_funct(sample):
    """ Plots a probability mass function from a sample of discrete random
    variables. """
    bars = sorted(Counter(sample).items())
    heights = [x[1]/len(sample) for x in bars]
    ticks = [x[0] for x in bars]
    plt.bar(range(len(heights)), heights, align='center')
    plt.xticks(range(len(ticks)), ticks)
    plt.show()


def random_discrete(a_list, p_list, n):
    sample = []
    # Complete this function
    return sample


a_list = [1, 3, 4]
p_list = [3/5, 1/5, 1/5]
sample = random_discrete(a_list, p_list, 10000)
plot_prob_mass_funct(sample)
