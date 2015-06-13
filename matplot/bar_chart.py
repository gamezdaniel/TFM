import matplotlib.pyplot as pyplt
import numpy as npy

# Collect data from file, avoid empty lines
with open('data_p.txt') as d:
    lines = [line.strip().split(' ') for line in d if len(line) > 1]

labels, y = zip(*lines)

# Indexes
ind = npy.arange(len(labels))

# Convert y values from str to int
y = map(int, y)

pyplt.figure()
pyplt.bar(ind, y, align='center')
pyplt.xticks(ind, labels, rotation=45)
pyplt.show()
