#!/usr/bin/env python3

import os
import sys
import gpustat
import random

stats = gpustat.GPUStatCollection.new_query()
ids = map(lambda gpu: int(gpu.entry['index']), stats)
ratios = map(lambda gpu: float(gpu.entry['memory.used'])/float(gpu.entry['memory.total']), stats)
pairs = list(zip(ids, ratios))
random.shuffle(pairs)
bestGPU = min(pairs, key=lambda x: x[1])[0]

print(f'Setting GPU to {bestGPU}', file=sys.stderr)
os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
os.environ['CUDA_VISIBLE_DEVICES'] = str(bestGPU)
print(f"export CUDA_VISIBLE_DEVICES={bestGPU}")
