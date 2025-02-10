# BachelorThesisLLM

## Overview

This repository contains the code and data for my bachelor thesis project, which focuses on fine-tuning machine learning models to predict the memorability of text. The project involves preprocessing data, training and fine-tuning models, and evaluating their performance. The scripts are provided as Jupyter Notebooks.

## Preconditions

1. You have to download the dataset from [here](https://www.cs.cornell.edu/~cristian/memorability_files/cornell_movie_quotes_corpus.zip) and have to extract it. Afterwards create a new folder in the root called "dataset" and put the file from the archive with the name "moviequotes.memorable_nonmemorable_pairs.txt" in there.

## Datasets

The dataset used in this project can be found and downloaded [here](https://www.cs.cornell.edu/~cristian/memorability.html).


# Requirements

You need to install the following requirements found in the [requirements.txt](./requirements.txt)
Additionally you need to run 
```shell
python -m spacy download en_core_web_sm
```
to download the used spacy dictionary

# Hardware

All calculations were performed on an RTX3060Ti.

# Additional info coming here

# Addition - Word based

Download the dataset available from [here](https://osf.io/spqjz/)

