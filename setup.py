#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for vo_hydro.

    This file was generated with PyScaffold 2.5.6, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import sys
from setuptools import setup

def setup_package():
    if 'docs' in sys.argv:
        setup(use_pyscaffold=False)
    else:
        setup(use_pyscaffold=True)

if __name__ == "__main__":
    setup_package()
