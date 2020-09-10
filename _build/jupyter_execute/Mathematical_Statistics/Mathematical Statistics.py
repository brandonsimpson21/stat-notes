


## T Distribution

Let $w \sim \mathcal{N}(0,1)$ and $v \sim \mathcal{\chi}^2(r)$ where $v$ and $w$ are independent

$$t = \frac{w}{\sqrt{\frac{v}{r}}}$$

find the joint distribution of $t$ and $u=v$ integerate out $u$  its a transformation problem

$$f_t(t)=\frac{\Gamma\left(\frac{r+1}{2}\right)}{\sqrt{\pi r} \;\Gamma\left(\frac{r}{2}\right)} \frac{1}{\left(1+ \frac{t^2}{r}\right)^{\frac{r+1}{2}}}$$ where $E[t]=0$ and $r>1$

$$var(t) = \frac{r}{r-2}$$ provided $r>2$

## F Distribution


let $u,v$ be independent rv's with $df=r_1,r_2$

$$F = \frac{\frac{u}{r_1}}{\frac{v}{r_2}} \sim F(r_1,r_2)$$

where $E[F]=\frac{r_1}{r_2-2}$ where $r_2>2$

$var[f] = \frac{2r_2^2(r_1+r_2-2)}{r_1(r_2-2)^2(r_2-4)}$ where $r_2>4$

## Students Theorem

recall $\bar{x} \sim \mathcal{N}(\mu,\frac{\sigma^2}{n})$ and $z=\frac{x-\mu}{\frac{\sigma}{\sqrt{n}}} \to \frac{\bar{x}-\mu}{\frac{s}{\sqrt{n}}}$

let $x_1 \cdots x_n$ be iid $\mathcal{N}(\mu, \sigma^2)$ and $s^2=\frac{\sum(x_i-\bar{x})^2}{n-1}$

1. $\bar{x} \sim \mathcal{N}(\mu,\frac{\sigma^2}{n})$ proof through mfg
2. $\bar{x}$ and $s^2$ are independent
3. $\frac{(n-1)s^2}{\sigma^2}\sim \mathcal{\chi}^2_{n-1}$
4. $t=\frac{\bar{x}-\mu}{\frac{s}{\sqrt{n}}} \sim T_{n-1}$

## Correlation

let $x_1 \cdots x_n$ and $y_1 \cdots y_n$ be rv's with well defined finite variance and $a_1\cdots a_n$ and $b_1 \cdots b_n$ be real constants

$t=\sum a_ix_i$ and $w=\sum b_iy_i$ then

$$cov(t,w)=\sum_{i=1}^n\sum_{j=1}^n a_ib_icov(x_i,y_i)$$ proof throw it into definition of covariance and use fact that expectation of sum is sum of expectation

## Unbiasdness
a statistic is unbiased if the expected value of the statistic is $\theta$

eg $\bar{x}$ is unbiased for $\mu$ since $E[\bar{x}]=\mu$

is $s^* = \frac{\sum(x_i-\bar{x})}{n}$ an unbiased estimator for $\sigma^2

note:
1. $\sum(x_i-\bar{x})^2=\sum(x_i-\bar{x})^2+n(\bar{x}-\mu)^2$
2. $var(x_i)=E[(x_i-\mu)^2=\sigma^2$
3. $var(\bar{x})=E[(\bar{x}-\mu)^2]=\frac{\sigma^2}{n}$

plug in for $E[s^*]$ and you get

$$\frac{n\sigma^2-n\frac{\sigma^2}{n}}{n} = \frac{(n-1)\sigma^2}{n} \neq \sigma^2$$

this is biased by $\frac{n-1}{n}$ so to make $s^*$ unbiased multiply by this thats wyc $s^2$ has $n-1$ in the denominator

WW2 tank example: suppose you have tanks with sequential serial numbers you have a sample of them and you want to figure out how many there are total
let $x\sim\mathcal{U}(0,\theta)$ we want to estimate $\theta$ using a random sample $x_1\cdots x_n$

naieve guess: $\hat{\theta}=max(x_n)$ is $\hat{\theta}$ unbiased?

we need the pdf for $\theta=max(x_1 \cdots x_n)$ so we need $E[\hat{\theta}]$

find the cdf for $\hat{\theta}$

\begin{align}
f_{\hat{\theta}} = p(\hat{\theta}\leq x)&=p(max(x_1\cdots x_n)\leq x)\\
&=p(x_1\leq x), x_2\leq x , \cdots , x_n\leq x) \text{since they are iid}\\
&=p(x_1 \leq x)^n\\
&=\left(\frac{x}{\theta}\right)^n
\end{align}

the pdf $f_{\hat{\theta}} = \frac{n\; x^{n-1}}{\theta^n}$ for $0 \leq x \leq \theta$

\begin{align}
E[\hat{\theta}] &= \int_0^\theta x \; \frac{n\;x^{n-1}}{\theta^n}dx\\
&=\frac{n}{\theta^n} \int_0^\theta x^n\\
&=\frac{n}{\theta^n}\left[\frac{x^{n-1}}{n+1}\right]_0^\theta
&=\left(\frac{n}{n+1}\right)\theta
\end{align}

sp its not unbiased, therefore

$\hat{\theta}^{best}=frac{n+1}{n} \; max(x_1, \cdots x_n)$

## Review

1. Chebyshevs inequality $p(|x-\mu|\geq k\sigma)\leq \frac{1}{k^2}$
2. triangle inequality $|A|+|B| \geq |A+B|$
3. $\epsilon, \delta$ definition of continuity of a real function $f$ at point $a$

$$\forall \epsilon>0 \; \exists \; \delta>0\; \text{st} \;|x-a|<\delta \; \text{then} \; |f(x)-f(a)|<\epsilon$$

## Convergence in Probability

Let $\{x_n\}$ be a sequence of rv's defined on a sample space $s$ we say $x_n$ converges in probability to $x$ if

$$\lim_{x\to \inf} (|x_n-x| \geq \epsilon)=0$$

or equivalently

$$\lim_{n\to \inf} p(|x_n-x| <\epsilon)=1$$

Theorem: suppose $x_n \overset{p}{\to}x$ and $a$ is a constant then $ax_n \overset{p}{\to} ax$

Theorem: suppose $x_n \overset{p}{\to}x$ and a real function g is continuous at $a$ then $g(x_n)\overset{p}{\to}g(a)$


## Weak Law of Large Numbers

Let $\{x_n\}$ be a sequence of rv's having common mean and variance st $\sigma^2 < \inf$
and $\bar{x_n}=\frac{\sum x_n}{n}$ then

$$\bar{x_n} \overset{p}{\to} \mu$$

proof:

let $\epsilon < 0$ be given then


$$p(|\bar{x}-\mu|>\epsilon) \leq \frac{\frac{\sigma^2}{n}}{\epsilon} \; \text{by chebyshev}$$

$\lim_{n \to \inf} p(|\bar{x_n} -\mu| \geq \epsilon \leq \lim_{n \to \inf}\frac{\sigma^2}{n \epsilon^2} =0$$$

## Consistent Estimators

let $x$ be a rv with cdf $f(x,\theta)$ let $x_1, \cdots , x_n$ be a random sample from the distribution of $x$
let $T_n$ be a statistic, then $t_n$ is a consistent estimator of $\theta$ if $t_n\overset{p}{\to} \theta$

Theorem: let $\{T_n\}$ be a sequence of estimators of a parameter with MSE $E[(t_n-\theta)^2]$ then the following are all true
1. if $E[(t_n-\theta)^2] \to 0$ then $t_n$ is a consistent estimator
2. $t_n$ is consistent if $E[t_n]\to \theta$ and $var(t_m)\to 0$
3. if $t_n$ is unbiased then $t_n$ is consistent if $var(t_n)\to 0 \; \forall \theta$

## Convergence In Distribution

let $\{x_n\}$ be a sequence of rv's  with pdf's $F_{x_n}$ and $F_x$
let $c(f_x)$ denote the set of all points where $F_x$ is continuous. $x_n$ converges in distribution (or law) if

$$\lim_{n\to \inf}F_{x_n}(x) = F_x(x) \; \forall \; x \; \in \; c(F_x)$$

Theorem: if the sequence converges in probability then it converges in distribution
Theorem: if sequence converges in distribution to a constant than it converges in probability to that constant
Theorem: if $x_n \overset{p}{\to} x$ and $g$ is a continuous function on the support of x then $g(x_n)\overset{D}{\to} g(x)$