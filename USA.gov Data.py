import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

path = 'datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]
# print(records[0])

frame = pd.DataFrame(records)
tz_counts = frame['tz'].value_counts()