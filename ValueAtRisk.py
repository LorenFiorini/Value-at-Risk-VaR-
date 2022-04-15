
# ARCH model
import numpy as np
import pandas as pd
from matplotlib import pyplot
from random import gauss
from random import seed
from arch import arch_model
from scipy.stats import binom


# Euro Dollar Exchange Rate (EUR USD) - Historical Chart (1999 - 2022)
# The data was downloaded from https://www.macrotrends.net/2548/euro-dollar-exchange-rate-historical-chart
data = pd.read_csv("euro-dollar-exchange-rate-historical-chart.csv", header = 8) 

data.tail()
