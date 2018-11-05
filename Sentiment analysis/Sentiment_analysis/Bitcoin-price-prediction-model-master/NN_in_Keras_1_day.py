

from keras.models import Sequential
from keras.layers import Dense

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from pytrends.request import TrendReq
import json, datetime
import requests
import csv

np.random.seed(7)
RANDOM_SEED = 42

def get_data():
	jsonfile = open('inf_processed', 'r')
	feature_vector_array_train = []
	feature_vector_array_predict = []
	price_array_train = []
	#price_array_predict = []
	l = jsonfile.read().split('\n')
	l.pop()
	print(len(l))
	for i in l:
		feature_vector = []
		j = json.loads(i)
		d = datetime.datetime.strptime(j["created_at"], '%Y-%m-%dT%H:%M:%S').date()
		feature_vector.append(j['sentiment']['neg'])
		feature_vector.append(j['sentiment']['neu'])
		feature_vector.append(j['sentiment']['pos'])
		feature_vector.append(j['sentiment']['compound'])
		if (d < datetime.datetime.today().date()):
			feature_vector_array_train.append(feature_vector)
			price_array_train.append(int(float(j['price'])/200))
		else:
			feature_vector_array_predict.append(feature_vector)
			#price_array_predict.append(int(float(j['price'])/200))

	feature_vector_array_train = np.array(feature_vector_array_train)
	price_array_train = np.array(price_array_train)
	feature_vector_array_predict = np.array(feature_vector_array_train)
	#price_array_predict = np.array(price_array_train)


	#print(feature_vector_array)
	N, M = feature_vector_array_train.shape
	feature_vector_array_train_X = np.ones((N, M + 1))
	feature_vector_array_train_X[:, 1:] = feature_vector_array_train

	N, M = feature_vector_array_predict.shape
	feature_vector_array_predict_X = np.ones((N, M + 1))
	feature_vector_array_predict_X[:, 1:] = feature_vector_array_predict

	# Convert into one-hot vectors
	# num_labels = len(np.unique(target))
	num_labels = max(price_array_train) + 1
	price_array_train_Y = np.eye(num_labels)[price_array_train]  # One liner trick!
	#price_array_predict_Y = np.eye(num_labels)[price_array_predict]

	#return train_test_split(all_X, all_Y, test_size=0.33, random_state=42)
	#print("Price_array_train")
	#print(price_array_train)
	#print("Price_array_train_Y")
	#print(price_array_train_Y)

	return feature_vector_array_train_X, feature_vector_array_predict_X, price_array_train_Y

def main():
    train_X, test_X, train_y = get_data()

    #print(train_y)

    model = Sequential()
    model.add(Dense(train_X.shape[1], input_dim=train_X.shape[1], activation='sigmoid'))
    model.add(Dense(256, activation='sigmoid'))
    model.add(Dense(train_y.shape[1], activation='sigmoid'))
    model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
    model.fit(train_X, train_y, epochs=150)

    #scores = model.evaluate(test_X, test_y)
    ##print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    #print("Test X:")
    #print(test_X)
    #print("Prediction of test X")
    prediction = model.predict(test_X)
    total = 0
    #print(prediction)
    for i in prediction:
    	val = 0
    	for j,k in enumerate(i):
    		val = val + (200*j+100)*k
    	total = total + val
    predicted_value = total/len(prediction)
    print(predicted_value)
    with open('Sentiment_analysis_1_day_prediction.csv', 'w') as f:
    	w = csv.writer(f)
    	w.writerow([predicted_value])
    	f.flush()

if __name__ == '__main__':
    main()
