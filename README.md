# setGPU

A small Python library that automatically sets `CUDA_VISIBLE_DEVICES`
to the least-loaded GPU on multi-GPU systems and can be used by:

1. Putting `import setGPU` before any import
   that will use a GPU like Torch, TensorFlow, or JAX.
2. Defining an alias such as
   `alias setGPU='eval $(python3 -m setGPU)'`
   and calling that to set the GPU in the shell before running
   another program that uses the GPU.

# Installation

```
pip install git+git://github.com/bamos/setGPU.git
```

# Dependencies

+ [Jongwook Choi's](https://wook.kr) [gpustat](https://github.com/wookayin/gpustat) library (`pip install gpustat`)

# Licensing

This code is in the public domain.
