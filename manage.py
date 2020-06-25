#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""App demo for run in k8s"""

__version__ = "0.0.1"
__author__ = "Andres Restrepo <andres.e.restrepo.a@gmail.com>"

from flask_restful import reqparse, abort, Api, Resource, request
from flask import Flask
from mpmath import mp

import os
import logging

app = Flask(__name__)
api = Api(app)

env_1 = os.getenv('ENV_1')
env_2 = os.getenv('ENV_2')

class Healthy(Resource):
    def get(self):
        status = {'status': 'up', 'Env 1':env_1}, 200
        logging.debug(status, extra={'site': 'SOCL'})
        return status

class UnHealthy(Resource):
    def get(self):
        status = {'status': 'down'}, 500
        logging.debug(status, extra={'site': 'SOCL'})
        return status

class RunTimeError(Resource):
    def get(self):
        os._exit(0)

class PiCalc(Resource):
    def get(self):
        pinumbers = request.args.get('pinumbers','1')
        mp.dps = pinumbers
        status = {'status': 'up', 'PiCalc':str(mp.pi)}, 200
        logging.debug(status, extra={'site': 'SOCL'})
        return status

api.add_resource(Healthy, "/probe/healthy")
api.add_resource(UnHealthy, "/probe/unhealthy")
api.add_resource(RunTimeError, "/probe/error")
api.add_resource(PiCalc, "/probe/pi")


if __name__ == '__main__':
    logging.info("App demo started")
    app.run()
