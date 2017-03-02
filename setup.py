from setuptools import find_packages, setup

setup(
    name='setGPU',
    version='0.0.2',
    description="A small Python library that automatically sets CUDA_VISIBLE_DEVICES to the least loaded GPU.",
    author='Brandon Amos',
    author_email='bamos@cs.cmu.edu',
    platforms=['any'],
    license="Apache 2.0",
    url='https://github.com/bamos/setGPU',
    py_modules=['setGPU'],
    install_requires=[
        'gpustat'
    ]
)
