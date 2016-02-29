import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

theta = 100
maxSize = 10000
doubleMean = np.array([])
meanPlusN = np.array([])
firstStat = np.array([])
firstLast = np.array([])
lastStat = np.array([])
sample = uniform.rvs(scale=theta, size=maxSize)
grid = np.array([])

for sampleSize in range(1, maxSize, 1):
	grid = np.append(grid, sampleSize)
    doubleMean = np.append(doubleMean, abs(2 * sample[:sampleSize].mean() - theta))
    meanPlusN = np.append(meanPlusN, abs((sampleSize + 1) * np.amin(sample[:sampleSize]) - theta))
    firstStat = np.append(firstStat, abs(sample[:sampleSize].mean() + np.amax(sample[:sampleSize]) / 2 - theta))
    firstLast = np.append(firstLast, abs(np.amax(sample[:sampleSize]) + np.amin(sample[:sampleSize]) - theta))
    lastStat = np.append(lastStat, abs(((sampleSize + 1) / (sampleSize)) * np.amin(sample[:sampleSize]) - theta))

plt.figure(figsize=(7, 4))
plt.plot(grid, doubleMean)
plt.plot(grid, firstStat)
plt.plot(grid, meanPlusN)
plt.plot(grid, firstLast)
plt.plot(grid, lastStat)
plt.ylim(0, 2)
plt.show() 
