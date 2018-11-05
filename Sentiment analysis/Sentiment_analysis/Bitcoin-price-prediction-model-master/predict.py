import pandas as pd
import numpy as np
import plotly 
import peakutils
plotly.tools.set_credentials_file(username='sonijigar', api_key='5QyOYUZdkMRHBl4UUtU8')
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv('price-sentiment.csv')

time_series = data['sentiment']
time_series = time_series.tolist()

df = data['date']

ind_arr = []
indp_arr = [] 

cb = np.array(time_series)
indices = peakutils.indexes((-cb), thres=0.02/max(cb), min_dist=0.1)
indices_peak = peakutils.indexes(cb, thres=0.02/max(cb), min_dist=0.1)
# signal graph
# all_peaks = indices + indices_peak
i = 0 
for x in indices:
  ind_arr.append(x)

for y in indices_peak:
  indp_arr.append(y)  

ind_arr.sort()
# print("all_peak",all_peak.array)
# print("indices_peak",ind_arr)

it = 0 
ts = []

count = 0;
for t in range(len(df)):
  
  if it in ind_arr:
    ts.append(1)
  elif it in indp_arr:
    ts.append(-1)
  else:
    ts.append(0)
  it = it + 1

# print("ts_array",ts) 

tr1 = go.Scatter(
# x = [df[j] for j in range(len(time_series))],
# y = ts,

x = [df[j] for j in range(len(time_series))],
y = data['signal'],

mode='markers',
    marker=dict(
        size=15,
        color='rgb(255,0,0)',
        symbol='circle'
    ),
    connectgaps=True,
name='signal'
  )
dtplot = [tr1]

layout = go.Layout(yaxis=dict(
        autorange=True
        # showgrid=False,
        # zeroline=False,
        # showline=False,
        # autotick=True,
        # ticks='',
        # showticklabels=False
    )
)
# layout={
#   yaxis: {range: [-180, -88]}
# }
fig = go.Figure(data=dtplot, layout=layout)
py.plot(fig, filename='signal-buy-sell')


# print("minimas",indices)
glob_x = indices;
glob_y = [time_series[j] for j in indices]

# print("y\n",[df[j] for j in indices])
trace1 = go.Scatter(
x=[df[j] for j in range(len(time_series))],
y=time_series,
mode='lines',
name='Sentiment'
	)
trace2 = go.Scatter(
	x=df[indices],
	
	y=[time_series[j] for j in indices],
	
	mode='markers',
    marker=dict(
        size=8,
        color='rgb(255,0,0)',
        symbol='dash'
    ),
    name='Detected valley'
	)
trace3 = go.Scatter(
  x=df[indices_peak],
  
  y=[time_series[j] for j in indices_peak],
  
  mode='markers',
    marker=dict(
        size=8,
        color='rgb(0,255,0)',
        symbol='cross'
    ),
    name='Detected Peaks'
  )



dataplot = [trace1, trace2, trace3]


# py.plot(dataplot, filename='sentiment-with-peaks')

# var layout={
#   yaxis: {range: [-180, -88]}
# }
# Plotly.newPlot('myDiv', data, layout);
dif = pd.read_csv('price-sentiment.csv')
sample_data_table = FF.create_table(dif.head())
# py.plot(sample_data_table, filename='data-table')

trace1 = go.Scatter(x = dif['date'], y = dif['price'],
                  name='Price Values', marker=dict(size=8,color='rgb(0,255,0)'))

trace2 = go.Scatter(x = dif['date'], y = 11000+dif['sentiment']*5000,
                  name='Scaled sentiment values', marker=dict(size=8,color='rgb(255,0,0)'))

# layout = go.Layout(title='Bitcoin Prices Over Time',
#                    plot_bgcolor='rgb(230, 230,230)', 
#                    showlegend=True)
# fig = go.Figure(data=[trace1, trace2], layout=layout)

data = [trace1, trace2]

# py.plot(data, filename='bitcoin-prices-sentiment')




df2 = pd.read_csv('price-sentiment.csv')

sample_data_table = FF.create_table(df2.head())
# py.plot(sample_data_table, filename='data-table')

trace = go.Scatter(x = df2['date'], y = df2['price'],
                  name='Price Values')
layout = go.Layout(title='Bitcoin Prices Over Time',
                   plot_bgcolor='rgb(230, 230,230)', 
                   showlegend=True)
fig = go.Figure(data=[trace], layout=layout)

# py.plot(fig, filename='bitcoin-prices')




df1 = pd.read_csv('features.csv')

sample_data_table = FF.create_table(df1.head())
# py.plot(sample_data_table, filename='sample-data-table')

trace = go.Scatter(x = df1['date'], y = df1['sentiment'],
                  name='Sentiment Values')
layout = go.Layout(title='Tweet Sentiments Over Time',
                   plot_bgcolor='rgb(230, 230,230)', 
                   showlegend=True)
fig = go.Figure(data=[trace], layout=layout)

# py.plot(fig, filename='apple-stock-prices')



df = pd.read_csv('feature.csv')
X = df.iloc[:, :-1]
y = df.iloc[:, -1:].values.ravel()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# print("x train is {0}".format(X_train))
# print("y train is {0}".format(y_train))
# print(len(y_train))
# print("x test is {0}".format(X_test))
# print("y test is {0}".format(y_test))
# Create linear regression object
#regr = linear_model.LogisticRegression()
regr = linear_model.LinearRegression()

# print(type(y_train[0]))
# Train the model using the training sets
regr.fit(X_train, map(lambda number:float(number),y_train))

# Make predictions using the testing set
y_pred = regr.predict(X_test)

# The coefficients
# print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_pred))

error = np.mean(y_pred != y_test)
# print(y_pred)
# print(y_test)
# print(error)


