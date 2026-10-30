# MaxGeomHash

This repository contains the code to recreate all results presented in the manuscript titled "MaxGeomHash bridges MinHash and FracMinHash for scalable similarity estimation using sub-linear k-mer sketching". This paper was accepted and presented in RECOMB-2026 (https://recomb.org/recomb2026/), and was later published in Genome Research (doi: 10.1101/gr.282217.126).

## Requirements

Installation for Python environment is through conda and pip. The C++ implementation needs to be downloaded and built separately, and the path to the bin folder needs to be added in the PATH variable. To install the C++ implementation, use the instructions available here: https://github.com/mahmudhera/kmer-sketch.

## Installation
After downloading the repository, `cd` to the repository path and run the following.
```
conda create -n maxgeom -y
conda activate maxgeom
pip install --file requirements.txt
export PYTHONPATH=$(pwd):$PYTHONPATH
export PATH=path-to-kmer-sketch-bin:$PATH
```

## Running experiments
```
bash all_commands.sh
```