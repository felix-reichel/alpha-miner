from setuptools import setup, find_packages

setup(
    name='alpha-miner',
    version='0.1.3',
    packages=find_packages(),
    author='Felix Reichel',
    author_email='kontakt@felixreichel.com',
    description='The alpha-miner package implements the α-algorithm for process mining, '
                'transforming event logs into petri nets.',
    long_description='The alpha-miner package implements the α-algorithm, a '
                     'foundational method in process mining developed by van der Aalst, Weijters, and Măruşter.'
                     'This algorithm analyzes event logs—collections of activity sequences—to infer causal ('
                     'Discovery Limitations: Loops of Length 1 or 2, Faulty petri nets due to non-required implicit '
                     'places, Missing local dependencies, Bias.) See: https://ieeexplore.ieee.org/document/1316839.'
                     'relationships between activities. It also outputs a resulting petri net.',
    long_description_content_type='text/markdown',
    url='https://github.com/felix-reichel/alpha-miner',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
