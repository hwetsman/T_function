# set up
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd


# set up streamlit welcome
st.markdown('**Welcome to the Threshold Function simulator.** \
Imagine everyone has a quality called threshold (T). Not everyone\'s T is the \
same. T is distributed through the population according to some distribution. This \
simulator assumes T is normally distributed in a population of 330 people in a \
movie theatre. T, in this case, is their threshold for running out of the \
theatre without knowing why just because others do. If one person got up and ran \
out, would you? What if five got up and ran? 10? What\'s your T? You may select \
the form of a normal function by which T is distributed in the population and \
the original number of exiting people. The script will plot the population exit. \
Later, other distributions will be added.')
# set up population of 330
N = 330
# select normal
dist_type = st.sidebar.radio(
    'Distribution of T', ['Normal', 'Pareto', 'Lognormal', 'Random(1-N)', 'Chisquare'])

if dist_type == 'Normal':
    step = 1
    # set up streamlit selection of normal curve by input mean and sd
    mean = st.sidebar.slider('Mean of Normal Distribution', min_value=10,
                             max_value=50, value=25, step=1)
    sd = st.sidebar.slider('sd of Normal Distribution', min_value=1,
                           max_value=15, value=5, step=step)
    # # set up streamlit selection of initial number to leave
    # exit = st.sidebar.slider('Initial Number of People to Leave',
    #                          min_value=1, max_value=5, value=1, step=1)
    # set up production of normal curve
    dist = np.random.normal(mean, sd, N)
    dist = [int(x) for x in dist]
    dist = np.array(dist)
    # get rid of negative values
    if dist.min() < 0:
        add = abs(dist.min())+1
        dist = [x+add for x in dist]
        dist = np.array(dist)
# set up pareto dist
elif dist_type == 'Pareto':
    step = .1
    alpha = st.sidebar.slider('Alpha (shape)', min_value=1.0, max_value=5.0, value=3.0, step=step)
    min = st.sidebar.slider('Minimum Sensitivity', min_value=1, max_value=5, value=1, step=1)
    dist = np.random.pareto(alpha, N)
    dist = [int(x)+min for x in dist]
    dist = np.array(dist)
# set up Randint dist
elif dist_type == 'Random(1-N)':
    max_t = st.sidebar.slider('Max T', min_value=2, max_value=N, value=int(N/2), step=1)
    min_t = st.sidebar.slider('Min T', min_value=1, max_value=5, value=1, step=1)
    step = 1
    dist = np.random.randint(min_t, max_t+1, N)
elif dist_type == "Chisquare":
    step = 1
    k = st.sidebar.slider('Degrees of Freedom', min_value=1,
                          max_value=10, value=5, step=1)
    # sd = st.sidebar.slider('sd of Underlying Normal Distribution', min_value=1,
    #                        max_value=3, value=2, step=1)
    dist = np.random.chisquare(k, size=N)
    dist = np.array([int(x)+1 for x in dist])
    st.write(dist)
    st.write(dist.min(), dist.max())

# set up streamlit selection of initial number to leave
exit = st.sidebar.slider('Initial Number of People to Leave',
                         min_value=1, max_value=5, value=1, step=1)

# display dist curve
sns.set_style("white")
fig, ax = plt.subplots()
fig = plt.figure()
plt.title('Distribution of T in Population')
bins = np.arange(dist.min(), dist.max()+step, step)
plt.hist(dist, bins=bins, color='b')
plt.xlabel('Threshold')
st.sidebar.pyplot(fig)


# create df of population
df = pd.DataFrame({'T': dist})
df = pd.DataFrame(df.groupby('T').size())
df.rename({0: 'Count'}, inplace=True, axis=1)
df.reset_index(inplace=True, drop=False)
print(df)

# calculate steps of exit
pop = [N]  # create empty list to addend
count = 0
while N > 0:
    # st.write(N, exit, df['T'].min())
    if exit >= df['T'].min():
        # st.write(df['T'].min(), exit)
        temp = df[df['T'] <= exit]
        df = df[df['T'] > exit]
        sum = temp.Count.sum()
        N = N-sum
        pop.append(N)
        print(pop)
        exit = exit + sum
        count = count + 1
    else:
        break

# display exit graph
l = len(pop)
print(l)
x_array = np.arange(0, l, 1)
print(x_array)
if l > 1:
    # fig = plt.figure(5,3)
    sns.set_style("darkgrid")
    fig2, ax2 = plt.subplots(figsize=(5, 2))
    # fig2 = plt.figure(2, 2)
    # fig2 = plt.figure(figsize=(2, 2))
    ax2.scatter(x_array, pop, s=5, c='b')
    ax2.set_ylim(-5, 335)
    plt.title('Population Remaining by Reaction Step')
    plt.ylabel('Population Remaining')
    plt.xlabel('Reaction Step')
    if x_array.size > 15:
        plt.xticks(np.array([x for x in x_array if x % 2 == 0]))
    else:
        plt.xticks(x_array)
    st.pyplot(fig2)
    if pop[-1] < 1:
        st.write('And no one was left to see the credits')
        st.write('--------------------------------------')
    else:
        st.write(f'And then it settles down. The other {pop[-1]} people enjoy the movie.')
else:
    st.write('No one leaves. Enjoy the movie!')
