import tensorflow as tf
import numpy as np
print(tf.VERSION)
print(tf.keras.__version__)

model = tf.keras.Sequential()
# Adds a densely-connected layer with 64 units to the model:
model.add(tf.keras.layers.Dense(64, activation='relu'))
# Add a softmax layer with 10 output units:
model.add(tf.keras.layers.Dense(2, activation='softmax'))

def main():
    filename = 'csv.tfrecords'
    dataset = tf.data.TFRecordDataset(filename)

    def _parse_function(example_proto):
        keys_to_features = {'continous_feature': tf.FixedLenFeature((23),tf.int64),
                            'label': tf.FixedLenFeature((1),tf.int64)}
        parsed_features = tf.parse_single_example(example_proto, keys_to_features)
        x=parsed_features['continous_feature']
        y=parsed_features['label']
        x = tf.cast(x, tf.float32)
        y = tf.cast(y, tf.float32)
        return x,y

    # Parse the record into tensors.
    dataset = dataset.map(_parse_function)
    # Shuffle the dataset
    dataset = dataset.shuffle(buffer_size=1)
    # Repeat the input indefinitly
    dataset = dataset.repeat()
    # Generate batches
    dataset = dataset.batch(512)

    def create_model():
        # model
        inputs = tf.keras.Input(shape=(23,))  # Returns a placeholder tensor

        # A layer instance is callable on a tensor, and returns a tensor.
        x = tf.keras.layers.Dense(64, activation='relu')(inputs)
        x = tf.keras.layers.Dense(32, activation='relu')(x)
        predictions = tf.keras.layers.Dense(1, activation='sigmoid')(x)

        model = tf.keras.Model(inputs=inputs, outputs=predictions)

        model.compile(optimizer=tf.train.AdamOptimizer(0.001),
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        return model

    model=create_model()
    # model.summary()
    # Don't forget to specify `steps_per_epoch` when calling `fit` on a dataset.
    iterator = dataset.make_one_shot_iterator()
    x, y = iterator.get_next()
    model.fit(x=x,y=y, epochs=1,steps_per_epoch=10000)


    # tf.keras.models.save_model(model,'keras_model',overwrite=True)
    # # model.save('keras_model')
    # new_model = tf.keras.models.load_model('keras_model')
    # new_model.summary()


    ############################
    dataset2 = tf.data.TFRecordDataset('test.tfrecord')
    def _parse_function(example_proto):
        keys_to_features = {'feature': tf.FixedLenFeature((23),tf.int64),
                            'label': tf.FixedLenFeature((1),tf.int64)}
        parsed_features = tf.parse_single_example(example_proto, keys_to_features)
        x=parsed_features['feature']
        # y=parsed_features['label']
        # x = tf.cast(x, tf.float32)
        # y = tf.cast(y, tf.float32)
        return x

    # Parse the record into tensors.
    dataset2 = dataset2.map(_parse_function)
    # Repeat the input indefinitly
    dataset2 = dataset2.repeat(1)
    # Generate batches
    dataset2 = dataset2.batch(3)

    iterator = dataset2.make_one_shot_iterator()
    t = iterator.get_next()
    sess = tf.Session()
    import csv
    wtr = csv.writer(open('out.csv', 'w'), delimiter=',', lineterminator='\n')
    while 1:
        try:
            a=sess.run([t])
            a=np.asarray(a)
            a=np.squeeze(a,axis=0)
            print(a.shape)
            res = model.predict(a)
            print(res)
            # print(res.tolist())
            # submission=np.concatenate((submission,res),axis=0)
            for x in res:
                wtr.writerow(x)
        except tf.errors.OutOfRangeError:
            print("End of dataset")  # ==> "End of dataset"
            break
    #
    # x=np.ones((3,23))
    # print(x.shape)
    # res=model.predict(x)
    # print(res)


if __name__ == "__main__":
    main()