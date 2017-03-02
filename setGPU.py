import os
import gpustat

stats = gpustat.GPUStatCollection.new_query()

bestRatio, bestGPU = 1.0, 0
for gpu in stats:
    ratio = float(gpu.entry['memory.used'])/float(gpu.entry['memory.total'])
    if ratio < bestRatio:
        bestRatio = ratio
        bestGPU = int(gpu.entry['index'])

print("setGPU: Setting GPU to: {}".format(bestGPU))
os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
os.environ['CUDA_VISIBLE_DEVICES'] = str(bestGPU)
