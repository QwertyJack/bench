#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 jack <jack@bogon>
#
# Distributed under terms of the MIT license.

"""
http load test using locust
"""

import six
from locust import HttpLocust, TaskSet, task

from config import config, DEBUG


class BenchBehavior(TaskSet):
    def _generator(self):
        data = {'header': 'hello', 'payload': 'world'}
        yield data

    def on_start(self):
        """init"""
        pass

    def on_stop(self):
        """clean up"""
        pass

    @task(1)
    def post(self):
        """send http POST request"""
        resp = self.client.post(config['path'], six.next(self._generator()))
        if DEBUG:
            print(resp.text)


class BenchClient(HttpLocust):
    task_set = BenchBehavior
    host = config['host']
    min_wait = config['wait']
    max_wait = config['wait']
    # wait_function = lambda self: random.expovariate(1)*1000
