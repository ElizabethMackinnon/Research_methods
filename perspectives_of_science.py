import numpy as np
import matplotlib.pyplot as plt 

# creating the dataset
data = {'Psychology':0.754, 'Neuroscience':0.778, 'Arts and Communication':0.7, 'Hard Sciences':0.705}
courses = list(data.keys())
values = list(data.values())

# Define the error values. This should be the same length as your data.
errors = [0.096, 0.109, 0.144, 0.122]

fig = plt.figure(figsize = (10, 5))

plt.rc('font', family='Times New Roman', size=12,)

# creating the bar plot with error bars
plt.bar(courses, values, color ='black', width = 0.4, yerr=errors, capsize=7, 
        error_kw=dict(ecolor='gray', lw=2, capsize=5, capthick=2))

font = {'family': 'Times New Roman',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        'style': 'italic',
        }

plt.title("Science Self-Efficacy", loc = 'left', fontdict = font)
plt.show()

# creating the dataset
data = {'Psychology':0.542, 'Neuroscience':0.464, 'Arts and Communication':0.502}
courses = list(data.keys())
values = list(data.values())

# Define the error values. This should be the same length as your data.
errors = [0.176, 0.141, 0.181]

fig = plt.figure(figsize = (10, 5))

plt.rc('font', family='Times New Roman', size=12,)

# creating the bar plot with error bars
plt.bar(courses, values, color ='black', width = 0.4, yerr=errors, capsize=7, 
        error_kw=dict(ecolor='gray', lw=2, capsize=5, capthick=2))

font = {'family': 'Times New Roman',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        'style': 'italic',
        }

plt.title("Science anxiety", loc = 'left', fontdict = font)
plt.show()