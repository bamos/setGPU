# setGPU

A small Python library that automatically sets `CUDA_VISIBLE_DEVICES`
to the least-loaded GPU on multi-GPU systems.

+ Installation: `pip install setGPU`
+ Usage: `import setGPU` before any import that will use a GPU like `torch` or `tensorflow`.

# Licensing

This code is in the public domain.
