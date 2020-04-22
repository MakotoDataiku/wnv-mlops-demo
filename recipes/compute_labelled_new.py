# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
westnile_by_Trap_prepared = dataiku.Dataset("westnile_by_Trap_prepared")
df = westnile_by_Trap_prepared.get_dataframe()



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

labelled_new_df = df[df.WnvPresent ] # Compute a Pandas dataframe to write into labelled_new
unlabelled_new_df = ... # Compute a Pandas dataframe to write into unlabelled_new


# Write recipe outputs
labelled_new = dataiku.Dataset("labelled_new")
labelled_new.write_with_schema(labelled_new_df)
unlabelled_new = dataiku.Dataset("unlabelled_new")
unlabelled_new.write_with_schema(unlabelled_new_df)
