# QuantGAN
My Columbia QuantGAN project


This is a project I worked on for my Deep Learning Course at Columbia. It is based on a paper published by Magnus Wiese of JP Morgan. The paper discusses using a GAN, a generative adversarial network,
to produce artifical time series that would mimic the behavior of real time series data.

The paper can be found here: https://arxiv.org/abs/1907.06673

In short, we know that traditional stochastic differential equation models assume that the increments are Brownian, meaning they are normally distributed. In practice, we know actual return data is not
normally distributed, and is instead heavy-tailed. Moreover, real data displays periods of volatility clustering, which is not true with simulated data from an SDE. An SDE simulation also fails to
showcase other real world behavior, like the escalator-up and elevator-down effect we see often in the stock market.

My project was based on creating a GAN in Python to be trained on time series data, to see if we could replicate and achieve the results discussed in the paper.
