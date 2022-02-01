# Threshold Function Simulator

Imagine you are sitting in a full theatre of 330 people. You're paying close
attention to the movie, because it's very good. Suddenly, out of the corner of
your eye, you see someone get up and run out. Maybe he got a phone call, or
maybe he really needs to go to the bathroom. You think, "It's probably nothing."
About 10 seconds later two more people get up and rush out. "What's going on
here," you think.

What's going on is a property distributed to everyone in the theatre called a
threshold, or T. Everyone has some number, at which they'll act. In this example
it's the number of people rushing out of a crowded theatre without explanation
before you think that there's something happening you don't know about, and you
better leave too.

But it could be a threshold for anything. Countries buying bitcoin, people buying
gold, workers quiting a company, people moving from a city - everyone has a
threshold for everything. But how is that threshold distributed?

Well, it's different for different thresholds and different populations. So,
I'll be working on this simulator so you can play for yourself.

The example below is people leaving a theatre, but it could just as well be
countries buying bitcoin as a treasury reserve asset. First one, then another,
then a couple more, and suddenly, everyone.


![Example Illustration](/Example.jpg)

## Use
clone the repo,

set up your venv,

then:
`pip3 install -r requirements.txt` and `streamlit run T_function.py`

Enjoy!
