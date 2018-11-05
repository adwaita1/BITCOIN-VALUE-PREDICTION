### Bitcoin Price Prediction Using Twitter Sentiment Analysis

### Team Members
Abhineet Gupta

Jigar Soni

Nikita Sengupta

Vineet Zunjarwad

### Setup for collecting older tweets
To bypass the limitation of the twitter API, that is to get tweets more than 2 weeks earlier, we have scrapped the original twitter web page using a JSON provider. By which we can use infinite scrolling and get the previous data directly.


1. `$ pip install -r requirements.txt`

2. `$ python Exporter.py --querysearch "europe refugees" --maxtweets 10000`

### Setup for running prediction script
1. Create a new virtual environment

    `$ virtualenv -p python3 venv`

    `$ source venv/bin/activate`

    `$ pip install -r requirements.txt`

2. To calculate algorithm accuracy you will need feature.csv that you cann be found [here](https://drive.google.com/open?id=1u3vL5zIk3wHX844ZlHreWMewkCCBRToq)

    `$ python predict.py`

### Algorithm accuracy
We have acheived Mean Square Error close to 33 over the span of roughly 650K records with 70-30 split using Logistic Regression model. 


### Final Output:
The final out of the analysis is a website which shows signals: (To buy or not to buy botcoins on particular day!)
This front-end server is a node JS server, deployed on Heroku.
The website link is: 
https://vast-headland-21279.herokuapp.com/

![screenshot from 2017-12-11 19-26-58](https://user-images.githubusercontent.com/12612087/33866115-b23a3f58-dea9-11e7-9971-be2d22ebecf3.png)

![screenshot from 2017-12-11 19-27-14](https://user-images.githubusercontent.com/12612087/33866123-b5ade9c8-dea9-11e7-94d7-41a77eec8504.png)

The signals are being calculated using peak/valley values and slope of the bitcoin stock price at that interval.

![screenshot from 2017-12-11 19-27-22](https://user-images.githubusercontent.com/12612087/33866128-b7de3ef0-dea9-11e7-97e2-9015e3bb696f.png)

### The outcome of our project:
Here 1 suggests buying signals, -1 suggests selling signals and 0 suggests to retain whatever amount you have!

![screenshot from 2017-12-11 19-28-43](https://user-images.githubusercontent.com/12612087/33866130-b96df864-dea9-11e7-81a4-e0518d1094b5.png)
