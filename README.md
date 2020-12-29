# Deploy ML Flask to Heroku

Click the button below to quickly clone and deploy into your own Heroku acount.
If you don't have one it'll prompt you to setup a free one.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

web site:
https://myappcav20202020.herokuapp.com/predict

Postman
link: https://myappcav20202020.herokuapp.com/api?&sepal_length=5.0&sepal_width=4.0&petal_length=1.5&petal_width=2.0
*configure: method POST-> body RAW -> Json

example input:
{
    "sepal_length":5.0,
    "sepal_width":4.2,
    "petal_length":1.5,
    "petal_width":5.5
}

output:

{
    "Prediction": "Iris-virginica"
}



