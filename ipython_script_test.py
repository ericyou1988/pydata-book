# def f(x, y, z):
#     return (x + y) / z
#
# a = 5
# b = 6
# c = 7.5
#
# result = f(a, b, c)

import numpy as np
import matplotlib.pyplot as plt
plt.plot(np.random.randn(50).cumsum())

import re
states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
          'south   carolina##', 'West virginia?']

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        print(value)
        value = re.sub('[!#?]', '', value)
        print(value)
        value = value.title()
        print(value)
        result.append(value)
    return result
clean_strings(states)
