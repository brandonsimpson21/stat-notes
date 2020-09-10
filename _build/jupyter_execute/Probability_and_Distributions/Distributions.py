

## Binomial And Bernoulli Distributions
suppose we toss a coin $n$ times let $x \in \{0, \cdots ,n\}$ be the number of heads. if the probability of heads is $\theta$ then $X$ has a binomial distribution denoted $X \sim Bin(n,\theta)$

$$Bin(k|n,\theta) \triangleq {n \choose k} \theta^k(1-\theta)^{n-k}$$

Where ${n \choose k} \triangleq \frac{n!}{(n-k)!k!}$ is the number of ways to choose $k$ items from $n$

## Multinomial

to model outcomes of tossing k-sided die, let $x=(x_1, \cdots ,x_K)$ be a random vector where $x_j$ is the number of times side $j$ occurs

$$mu(x|n\theta) \triangleq {n \choose x_1,\cdots x_K}\prod_{j=1}^K\theta_j^{x_j}$$

if we one hot encode the states the pmf becomes

$$mu(x|1,\theta)\triangleq \prod_{j=1}^K\theta_j^{\mathbb{I}(x_j=1)}$$

which we denote $Cat(x|\theta)$

## Poisson
often used for modeling counts of rare events.

$x\in\{0,1,2,\cdots\}$ has a poisson distribution with paramter $\lambda > o$

$$Poi(x|\lambda)= e^{-\lambda}\frac{\lambda^x}{x!}$$