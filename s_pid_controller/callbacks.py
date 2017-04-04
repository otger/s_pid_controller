#!/usr/bin/python
# -*- coding: utf-8 -*-
from entropyfw import Callback, CallbackFactory

"""
callbacks
Created by otger on 23/03/17.
All rights reserved.
"""


class UpdatePID(Callback):
    name = 'udpate_pid'
    description = "Update a pid input value"
    version = "0.1"

    def __init__(self, event, manager, module):
        Callback.__init__(self, event, manager, module)
        self.input_key = None
        self.output_event = None

    def get_input_value(self):
        if self.input_key:
            return self.event.value[self.input_key]
        return self.event.value

    def functionality(self):
        new_output = self.module.update_pid_input(self.output_event, self.get_input_value())
        self.module.pub_event(self.output_event, new_output)


class PIDFactoryCallbacks(CallbackFactory):
    def __init__(self, input_key, output_event):
        self.input_key = input_key
        self.output_event = output_event

    def get_cb(self, event, manager, module):
        inst = UpdatePID(event=event, manager=manager, module=module)
        inst.input_key = self.input_key
        inst.output_event = self.output_event
        return inst
