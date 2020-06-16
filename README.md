# GIPFA

This project includes the code of the Artificial Neural Network used for the [GIPFA](https://arxiv.org/abs/2006.07573) paper, which allows generating International Phonetic Alphabet (IPA) pronunciation from an audio file.

![](gipfa.png?raw=true)

## Installation

* Download files on your machine
  * git clone https://github.com/marxav/gipfa.git

* Go to the gipfa main directory
  * cd gipfa

* Create a virtual environment
  * python3 -m venv gipfa

* Activate virtual environment
  * source gipfa/bin/activate

* Load the python librairies needed for GIPFA from the requirements file
  * python3 -m pip install -r requirements.txt

## Run files

In order to run this code, you need to:
* Run the [make_local_database.ipynb](make_local_database.ipynb) python script in a Jupyter notebook. This script downloads the dataset made of a .CSV file (5 MB) as well as 80,260 audio .WAV files (9 GB).
* Run the [gipfa.ipynb](gipfa.ipynb) in order to create the ANN model, train it, test it and display the results of the paper.
