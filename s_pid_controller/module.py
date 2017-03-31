#!/usr/bin/python
# -*- coding: utf-8 -*-
from entropyfw import Module
from pidcontroller import PIDController
from .callbacks import PIDFactoryCallbacks
# from .actions import StartTempLoop, EnableChannel, StopTempLoop
from .web.api.resources import get_api_resources

"""
module
Created by otger on 23/03/17.
All rights reserved.
"""


class EntropyPIDController(Module):
    name = 'pidcontroller'

    def __init__(self, name=None, channels=list(range(9))):
        Module.__init__(self, name=name)
        self.pid_manager = PIDManager()
        # self.register_action(EnableChannel)
        for r in get_api_resources():
            self.register_api_resource(r)

    def register_pid(self, output_event, input_event, input_key=None, flags=0):
        """
        This method creates a new PID controller which will subscribe to events on 'input_event'
        and will generate 'output_event' named events. 'output_event' must
        be different for all PID generated as it is used as a unique identifier, and it will make
        no sense that two different pid controllers published same events.

        'output_event' events contain on its value field the new actuator value to be applied.

        :param output_event: event name to be published after each update on the PID input
        :param input_event: event regular expression that carries sensor value information
        :param input_key: in case event publishes a dictionary, which key is the one with the
                          sensor information
        :param flags: flags for input_event regular expression
        :return: None
        """
        self.pid_manager.new_pid(output_event)
        self.register_callback(PIDFactoryCallbacks(input_key=input_key, output_event=output_event),
                               pattern=input_event, flags=flags)

    def configure_pid(self, pid_identifier, kp, ki=0, kd=0, setpoint=0, output_range=(0, 100)):
        pid_controller = self.pid_manager.get_controller(pid_identifier)
        pid_controller.kp = kp
        pid_controller.ki = ki
        pid_controller.kd = kd
        pid_controller.setpoint = setpoint
        pid_controller.output_range = output_range

    def set_pid_setpoint(self, pid_identifier, setpoint):
        pid_controller = self.pid_manager.get_controller(pid_identifier)
        pid_controller.setpoint = setpoint

    def update_pid_input(self, pid_identifier, input_value):
        """Update new input value for a pid and get its new output value"""
        pid_controller = self.pid_manager.get_controller(pid_identifier)
        return pid_controller.update(input_value)

    def get_pid_status(self, pid_identifier):
        pid_controller = self.pid_manager.get_controller(pid_identifier)
        return pid_controller.status


class PIDManager(object):

    def __init__(self):
        self._controllers = {}

    def new_pid(self, name):
        if name in self._controllers:
            raise Exception('There is already a PID Controller named {0}'.format(name))
        self._controllers[name] = PIDController(kp=0, ki=0, kd=0)
        return self._controllers[name]

    def get_controller(self, pid_identifier):
        if pid_identifier not in self._controllers:
            raise Exception('There is no PID Controller named {0}'.format(pid_identifier))
        return self._controllers[pid_identifier]