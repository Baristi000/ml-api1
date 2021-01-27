import tensorflow as tf
from core.config import setting
import numpy as np

def train_bin(data:list, label:list, name:str, percent: float):
    name = name+str(len(setting.var_learn1))
    train_values = data
    train_labels = label
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(2,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dropout(.3),
        tf.keras.layers.Dense(2, activation='softmax')
    ])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

    times = 0
    acc = 0    
    while times < 100 and acc < percent:
        times+=1
        model.fit(train_values, train_labels, epochs=1)
        loss,acc = model.evaluate(train_values, train_labels, verbose = True)

    setting.var_learn1.update({name:model})

    return {"times_train":times,
            'percent':acc}

def predict_bin(data:list, name:str):
    r = setting.var_learn1[name].predict(data)
    result = {}
    for i in range(len(r)):
        result.update({int(np.argmax(r[i])):str(data[i])})
    return {'predict':result}