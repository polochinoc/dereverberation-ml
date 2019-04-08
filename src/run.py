# -*- coding: utf-8 -*-

import src.utils.logger as log
from src.datagen.io import generate_dataset, _export
from src.utils.data import write_data, read_data
#from src.neuralnet.utils import shape, unshape
#from src.neuralnet.model import NeuralNetwork


def run(dry_dpath, fx_dpath, output_dir=None):
    # Dataset generation

    log.info('Generating dataset of wet samples')
    
    generate_dataset(dry_dpath, fx_dpath, output_dir)
    
    # Shaping and storing data

    log.info('Retrieving data and saving it into a numpy file')
 
    write_data()

    # Reading data

    log.info('Reading data from numpy file')

    data, labels = read_data()

    """
    # Model training

    log.info('Training the model')

    NN = NeuralNetwork()
    NN.compile()
    data, labels = map(shape, (data, labels))
    NN.train(data[:-10], labels[:-10])
    NN.save()

    # Model predicting

    log.info('Predicting ')

    res = NN.predict(data[-10:])
    _export(unshape(res))
    """
