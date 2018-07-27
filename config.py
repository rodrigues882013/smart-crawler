#!/usr/bin/env python

import os
import yaml

with open(os.path.join(os.path.dirname(__file__), "config.yml"), 'r') as f:
    settings = yaml.load(f)
