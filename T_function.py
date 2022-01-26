# set up
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd


# set up streamlit welcome
st.write('Welcome to the Threshold Function simulator. The Threshold Function is \
a theoretical construct in population science. The paradigm this simulator is based \
on is the crowded theatre. Imagine a theatre of 330 people. Suddenly some number \
of people get up and leave. Everyone sees them leave. Depending on some threshold, \
T, which each individual has, each individual will react once their T of quickly \
exiting people is reached. You may select the form of a normal function by which \
T is distributed in the population and the original number of exiting people. The \
script will plot the population exit. Later, other distributions will be added.')
# set up population of 330
N = 330
# select normal
st.sidebar.radio('Distribution of T', ['Normal'])
# set up streamlit selection of normal curve by input mean and sd
mean = st.sidebar.slider('Mean of Normal Distribution', min_value=10,
                         max_value=50, value=25, step=1)
sd = st.sidebar.slider('sd of Normal Distribution', min_value=1, max_value=15, value=5, step=1)
# set up streamlit selection of initial number to leave
exit = st.sidebar.slider('Initial Number of People to Leave',
                         min_value=1, max_value=5, value=1, step=1)
# set up production of normal curve
dist = np.random.normal(mean, sd, N)
dist = [int(x) for x in dist]
dist = np.array(dist)
# get rid of negative values
if dist.min() < 0:
    add = abs(dist.min())+1
    dist = [x+add for x in dist]
    dist = np.array(dist)

# display normal curve
fig, ax = plt.subplots()
plt.figure(figsize=(2, 4))
step = 2
bins = np.arange(dist.min(), dist.max()+step, step)
ax.hist(dist, bins=bins)
st.sidebar.pyplot(fig)

# create df of population
df = pd.DataFrame({'T': dist})
df = pd.DataFrame(df.groupby('T').size())
df.rename({0: 'Count'}, inplace=True, axis=1)
df.reset_index(inplace=True, drop=False)
print(df)

# calculate steps of exit
pop = [N]  # create empty list to addend
#st.write('starting pop', N)
#st.write('first exit', exit)
# st.write('________________-')
count = 0
while N > 0:
    #st.write(count, 'pop left', N)
    #st.write('Threshold min', df['T'].min())
    if exit > df['T'].min():
        temp = df[df['T'] <= exit]
        df = df[df['T'] > exit]
        sum = temp.Count.sum()
        #st.write('leaving', sum)
        N = N-sum
        #st.write('pop left', N)
        pop.append(N)
        print(pop)
        exit = exit + sum
        #st.write('exited', exit)
        #st.write('min threshold', df['T'].min())
        count = count + 1
    else:
        # st.write("No one leaves. Enjoy the movie!")
        break

# display exit graph
l = len(pop)
print(l)
x_array = np.arange(0, l, 1)
print(x_array)
if l > 1:
    fig, ax = plt.subplots()
    plt.figure(figsize=(6, 3))
    ax.scatter(x_array, pop)
    st.pyplot(fig)
    if pop[-1] < 1:
        st.write('And no one was left to see the credits')
    else:
        st.write(f'And then it settles down. The other {pop[-1]} people enjoy the movie.')
else:
    st.write('No one leaves. Enjoy the movie!')
