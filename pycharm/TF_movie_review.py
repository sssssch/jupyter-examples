# -*-coding:utf-8-*-
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

train_data, validation_data, test_data = tfds.load(
    name="imdb_reviews",
    split=('train[:80%]', 'train[20%:]', 'test'),
    as_supervised=True)


train_examples_batch, train_labels_batch = next(iter(train_data.batch(10)))
train_examples_batch

train_labels_batch

embedding = "https://hub.tensorflow.google.cn/google/tf2-preview/gnews-swivel-20dim/1"
hub_layer = hub.KerasLayer(embedding, input_shape=[],
                           dtype=tf.string, trainable=True)

hub_layer(train_examples_batch[:3])


model = tf.keras.Sequential()
model.add(hub_layer)
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(1))

model.summary()


model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

early_stoping = tf.keras.callbacks.EarlyStopping()

history = model.fit(train_data.shuffle(10000).batch(512),
                    epochs=20,
                    callbacks=[early_stoping],
                    validation_data=validation_data.batch(512),
                    verbose=2)

results = model.evaluate(test_data.batch(512), verbose=2)

for name, value in zip(model.metrics_names, results):
    print("%s: %.3f" % (name, value))
