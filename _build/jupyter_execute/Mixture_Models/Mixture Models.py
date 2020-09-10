

Latent Variable Models assume that the observed variables are correlated because they arise from a hidden common 'cause' and have two main advantages

1. they often have fewer parameters than models that directly represent correlation in the visible space

2. serve as a bottleneck which computes a compressed representation of the data

The simplest form is when $z_i \in \{1, \cdots , K\}$ represents the discrete latent state using a discrete prior $p(z_i)=Cat(\pi)$ and a liklihood $p(x_i|z_i=k)=p_k(x_i)$ where $p_k$ is the $k^{th}$ base distribution we mix together $K$ base distributions as follows

$$p(x_i|\theta)=\sum_{k=1}^K\pi_k\;p_k(x_i|\theta)$$

where $0<\pi_k<1$ and  $\sum_{k=1}^K\pi_k=1$

## Mixture of Gaussians

the most common mixutre model is a multivariate gaussian (GMM) with mean $\mu_k$ and covariance matrix $\Sigma_k$ the model has the form

$$p(x_i|\theta)=\sum_{k=1}^K\pi_k\; \mathcal{N}(x_i|\mu_k,\Sigma_k)$$

