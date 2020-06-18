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
  
* Download the dataset (size=1.2Go)
  * python3 download_dataset.py

## Evaluation and Training

In order to run this code, you need to:
* Run the [gipfa.ipynb](gipfa.ipynb) in order to create the ANN model, train it, test it and display the results of the paper.

## Results

GIPFA achieves the following performance:

### 

| Tested samples | Mean Accuracy |
| -------------- | ------------- |   
|     1000       |     75.0      | 

The detailed performance is availaible in this [CSV file](https://fonétik.fr/fr_wiktionary_excerpt_results.csv) (with '\t' as a separator)

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
