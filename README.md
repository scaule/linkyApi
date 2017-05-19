# Linky Api

## Getting Started

This project help you to install your own linky (enedis, edf) api to with python to fetch your own
electric consumption and use it like you want.

### Prerequisites

Only Python and Flask


### Installing

```
pip install Flask
```

## Deployment

You only have to install all files on your servers and use :

```
python app.py
```

This start a new server on port 5000

## Using it on your navigator

http://serverIp:5000/consumption/month?login=your_login&password=your_password&start=01/04/2017&end=30/05/2017

## Built With

* [Flask](http://flask.pocoo.org/) - Flask is a microframework for Python based on Werkzeug

## Authors

***Caule Simon **



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Inspired by (if you have to check your consumption in your kindle it's for you) : https://github.com/outadoc/linkindle