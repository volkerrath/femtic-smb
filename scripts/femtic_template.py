#!/usr/bin/env python3

"""
Reads ModEM's Jacobian, does fancy things.

@author: vrath   Feb 2021

"""

# Import required modules

import os
import sys

import time
from datetime import datetime
import warnings

import numpy as np
import netCDF4 as nc

from numba import njit

FEMTIC_DATA = os.environ["FEMTIC_DATA"]
FEMTIC_ROOT = os.environ["FEMTIC_ROOT"]

mypath = [FEMTIC_ROOT+"/modules/", FEMTIC_ROOT+"/scripts/"]
for pth in mypath:
    if pth not in sys.path:
        sys.path.insert(0,pth)


import jacproc as jac
import modem as mod
from version import versionstrg
import util as utl

version, _ = versionstrg()
titstrng = utl.print_title(version=version, fname=__file__, out=False)
print(titstrng+"\n\n")

