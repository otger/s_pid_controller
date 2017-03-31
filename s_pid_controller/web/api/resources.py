#!/usr/bin/python
# -*- coding: utf-8 -*-
from entropyfw.api.rest import ModuleResource
from flask import jsonify
from flask_restful import reqparse
from entropyfw.common import get_utc_ts
from PicoController.common.definitions import THERMOCOUPLES, UNITS

"""
resources
Created by otger on 29/03/17.
All rights reserved.
"""


class RegisterNewPID(ModuleResource):
    url = 'register_pid'
    description = "Register a new PID Controller into an event"

    def __init__(self, module):
        super(RegisterNewPID, self).__init__(module)
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('output_event', type=str, required=True, location='json')
        self.reqparse.add_argument('input_event', type=str, required=True, location='json')
        self.reqparse.add_argument('input_key', type=str, location='json')
        self.reqparse.add_argument('flags', type=int, location='json')

    def post(self):
        args = self.reqparse.parse_args()
        self.module.register_pid(output_event=args['output_event'],
                                 input_event=args.get('input_event'),
                                 input_key=args.get('input_key', None),
                                 flags=args.get('flags', 0))

        return jsonify({'args': args,
                        'utc_ts': get_utc_ts(),
                        'result': 'done'})


def get_api_resources():
    return [RegisterNewPID]
