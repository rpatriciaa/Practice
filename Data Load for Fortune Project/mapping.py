import sys
from numpy import inner
import pandas as pd
from postgres import connect


def mapping(data,id):
    merged = pd.merge(data,id)
    return merged