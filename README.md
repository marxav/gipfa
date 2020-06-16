# GIPFA

This repository is the official implementation of [GIPFA: Generating IPA Pronunciation from Audio](https://arxiv.org/abs/2006.07573).

![](gipfa.png?raw=true)

## Requirements

* Require Ubuntu 18.04, Python 3.6+.

* Download files on your machine
  * git clone https://github.com/marxav/gipfa.git

* Go to the gipfa main directory
  * cd gipfa

* Create a virtual environment
  * python3 -m venv gipfa

* Activate virtual environment
  * source gipfa/bin/activate

* Load the python librairies needed for GIPFA (e.g. numpy, pandas, torch...) from the requirements file
  * python3 -m pip install -r requirements.txt

## Datasets

We will publish the following datasets, all data originally coming from Wikimedia Commons and Wikimedia French Wiktionary:
* [fr_wiktionary_excerpt.csv](https://fonétik.fr/fr_wiktionary_excerpt.csv)
* audio files (link will be availabe soon)

* In the meantime, run the [make_local_database.ipynb](make_local_database.ipynb) python script in a Jupyter notebook. This script downloads the dataset made of a .CSV file (5 MB) as well as 80,260 audio .WAV files (9 GB).


## Evaluation and Training

In order to run this code, you need to:
* Run the [gipfa.ipynb](gipfa.ipynb) in order to create the ANN model, train it, test it and display the results of the paper.

## Results

GIPFA achieves the following performance:

### 

| Tested samples | Mean Accuracy |
| -------------- | ------------- |   
|     1000       |     75.0      | 

## License

GIPFA is released under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Citation
The pipeline is described in the following paper:
```bibtex
@misc{marjou2020gipfa,
    title={GIPFA: Generating IPA Pronunciation from Audio},
    author={Xavier Marjou},
    year={2020},
    eprint={2006.07573},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
