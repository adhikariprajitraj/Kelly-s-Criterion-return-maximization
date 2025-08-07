# Kelly's Criterion for Multiple Discrete Outcomes
> Prajit Adhikari


Suppose we are betting on something that has more than two possible outcomes, the Kelly Criterion is given by 

$$
f = \arg \max \displaystyle{\sum_{i=1}^n} p_i \log(1+f \cdot b_i)
$$

Where
- $p_i$ is the probability of the outcome $i$
- $b_i$ is the return multiple if outcome $i$ happens
- $f$ is the fraction of bet for each outcome


I am first going to explore some data on the internet for betting and extract them and try implementing the Kelly's Criterion in that set of data. 