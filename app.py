#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from linky import Linky
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/consumption/year')
def getConsumptionPerYear():
    linky = Linky(request.args.get('login'),request.args.get('password'))
    return jsonify(linky.getConsumptionPerYear())

@app.route('/consumption/month')
def getConsumptionPerMonth():
    linky = Linky(request.args.get('login'),request.args.get('password'))
    return jsonify(linky.getConsumptionPerMonth(request.args.get('start'), request.args.get('end')))

@app.route('/consumption/day')
def getConsumptionPerDay():
    linky = Linky(request.args.get('login'),request.args.get('password'))
    return jsonify(linky.getConsumptionPerDay(request.args.get('start'), request.args.get('end')))


@app.route('/consumption/hour')
def getConsumptionPerHour():
    linky = Linky(request.args.get('login'),request.args.get('password'))
    return jsonify(linky.getConsumptionPerHour(request.args.get('start'), request.args.get('end')))

if __name__ == '__main__':
    app.run(debug=True)

