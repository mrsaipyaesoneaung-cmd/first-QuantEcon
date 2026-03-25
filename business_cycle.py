import matplotlib.pyplot as plt
import pandas as pd
import datetime
import wbgapi as wb
import pandas_datareader.data as web

# Set graphical parameters
# #some minor code to help with colors in our plots.
cycler = plt.cycler(
    linestyle=["-", "-.", "--", ":"], color=["#377eb8", "#ff7f00", "#4daf4a", "#ff334f"]
)
plt.rc("axes", prop_cycle=cycler)
