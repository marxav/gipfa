#!/usr/bin/env python
# coding: utf-8

# The goal of this file is to download the dataset coming as 
# a unique tar file containing
#   * a readme-40.txt file indicating the licences
#   * a fr_wiktionary_excerpt.csv audio (excerpt of Wiktionary data)
#   * audio samples from Wikimedia Commons compressed as MFCC files
# 
# The needed disk space is approximately:
# * 1.2Go (if mfcc==40)
# * 0.5Go (if mfcc==13)


import os
import requests
import tarfile


CONFIG = {
    'csv_server': 'https://fonetik.fr',
    'archive_file': 'gipfa.tar',    
    'dictionary_source_file': 'fr_wiktionary_excerpt.csv',    
    'root_dir': '.',
    'mfcc': 40,
}

CONFIG['audio_dir'] = CONFIG['root_dir'] + '/' + 'audio'
new_suffix = '-' + str(CONFIG['mfcc']) + '.'
CONFIG['archive_file'] = CONFIG['archive_file'].replace('.', new_suffix)
config = CONFIG


def download_archive():
    
    # download the dataset locally
    filename = config['archive_file']
    url_file = config['csv_server'] + '/' + filename
    if not os.path.exists(filename):
        # unfortunately wget does not work because of a redirection
        # with the server containing the CSV
        # so wget.download(url_file) doe not work
        print('downloading %s' % filename)
        r = requests.get(url_file, allow_redirects=True)
        with open(filename, 'wb') as f:
            f.write(r.content)


def extract_files():
    filename = config['archive_file']
    archive = tarfile.open(filename)
    archive.extractall()
    os.remove(filename)


def main():
    download_archive()
    extract_files()


if __name__ == "__main__":
    main()

