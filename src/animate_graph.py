# Parts of the code based on repository: https://github.com/lucs123/sorting-visualizer-matplotlib

import matplotlib.pyplot as plt
from celluloid import Camera


fig = plt.figure()
camera = Camera(fig)
comparisons = 0


def plot(highlight, data):
    arr = list(range(len(data)))
    global comparisons
    comparisons += 1
    
    colors = list(len(data) * "b")
    colors[highlight] = "r"
    plt.bar(arr, data, color=colors)
    
    camera.snap()