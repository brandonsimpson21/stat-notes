

## Joint Distributions

$$p(A,B)=p(A|B)p(B)$$

### Marginal Distrubtion

given a joint distribution we define the marginal distribution as

$$p(A)=\sum_bp(a,b)=\sum_bp(A|B=b)\;p(B=b)$$

### Chain Rule of Probability

$$p(x_{1:D})=p(X_1)p(x_2|X_1)p(X_3|X_2,X_1)\cdots p(X_D|X_{1:d-1})$$

### Conditional Probability

$$p(A|B)=\frac{p(A,B)}{p(B)}$$ if $B>0$

## Bayes Rule

$$p(X=x|Y=y)=\frac{p(X=x)p(Y=y)}{p(Y=y)})=\frac{p(X=x)pY=y|X=x)}{\sum_{x^\prime{}}p(X=x^\prime)p(Y=y|X=x^\prime)} $$


## Independence & Conditional Independence

$X$ and $Y$ are unconditionall independent or marginally independent denoted $X\perp Y$ if ew can represent the joint as the product of the two marginals

$$X\perp Y \iff p(x,y)=p(X)p(Y)$$

we say $X$ and $Y$ are conditionall independent given $Z$ iff the conditional joint can be written as the product of conditional marginals

$$X \perp Y |Z \iff p(X,Y|Z)=p(X|Z)p(Y|Z)$$

it is also true that $X\perp Y |Z$ iff there exist functions $g$ and $h$ such that

$$p(x,y|z)=g(x,z)h(y,z)\; \forall \; x,y,z \;st\;p(z)>0$$

## Covariance And Correlation

the covariance between two rv's $X$ and $Y$ measures the degree to which $X$ and $Y$ are linearly related

$$cov[X,Y]\triangleq \mathbb{E}[(X-\mathbb{E}[X])(Y-\mathbb{E}Y)]=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]$$

if $x$ is a d-dimensional random vector its covariance matriz is defined by the following symmetric positive definite matrix

\begin{align}
    cov[x] &\triangleq \mathbb{E}\left[(x-\mathbb{E}[x])(x-\mathbb{E}[x])^T\right]\\
    &=
\end{align}

$0\leq cov\leq \inf$

sometimes its easier to work with a normalized measure with a finite upper bound the pearson correlation coefficient between $X$ and $Y$ is

$$corr[X,Y] \triangleq \frac{cov[X,Y]}{\sqrt{var[X]var[Y]}}$$ where $-1\leq corr[X,Y] \leq 1 $

## Transformations of Random Variables

if $x \sim p()$ is some rv and $y=f(x)$ what is the distribution of $y$? we can use the change of variable formula

$$p_y(y)=p_x(x)\left|\frac{dx}{dy}\right|$$

for multivariate change of variables

let $f$ be a function that maps $\mathbb{R}^n$ to $\mathbb{R}^n$ and let $y=f(x)$ than its jabobian matrix $J$ is given by

$$J_{x\to y} \triangleq \frac{\partial(y_y, \cdots ,y_n)}{\partial{(x_1, \cdots , x_n)}} \triangleq$$

# todo bmatrix has issues in jupyter



## Entropy

the entropy of a rv $X$ with distribution $p$ denoted $\mathbb{H}(X)$ for a discrete distribution with $K$ states

$$\mathbb{H}(X) \triangleq -\sum_{k=1}^K p(X=k)log_2p(X=k)$$

## Kullback-Leibler Divergence


