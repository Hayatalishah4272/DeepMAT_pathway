# -*- coding: utf-8 -*-
"""Training & Testing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qy4r1ABFFbup320kfDUivP1Fzt3H9mAP

Training testing and validation of the model
"""

train_dataset = MPNNDataset(x_train, y_train)
valid_dataset = MPNNDataset(x_valid, y_valid)
test_dataset = MPNNDataset(x_test, y_test)

history = mpnn.fit(
    train_dataset,
    validation_data=valid_dataset,
    epochs=100,
    verbose=2,
    class_weight={0: 2.0, 1: 0.5},
)