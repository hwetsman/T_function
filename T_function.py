# set up
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


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
                         max_value=100, value=50, step=1)
sd = st.sidebar.slider('sd of Normal Distribution', min_value=1, max_value=20, value=5, step=1)
# set up streamlit selection of initial number to leave
st.sidebar.slider('Initial Number of People to Leave', min_value=1, max_value=5, value=1, step=1)
# set up production of normal curve
dist = np.random.normal(mean, sd, N)
dist = [int(x) for x in dist]
st.write(dist)

# display normal curve
# calculate steps of exit
# display exit graph
