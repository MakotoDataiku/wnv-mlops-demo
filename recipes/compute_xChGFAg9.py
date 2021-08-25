# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
test = dataiku.Dataset("test")
test_df = test.get_dataframe()


# Write recipe outputs
heatmap = dataiku.Folder("xChGFAg9")
heatmap_info = heatmap.get_info()
