

# Generalized Additive Models

has the form

$$f(x) - \alpha + f_1(x_1) + \cdots + f_D(x_D)$$

each $f_j$ can be modeled by some scatterplot smoother and $f(x)$ can be mapped to $p(y|x)$ using a link function

it is typical to use smoothing splines for $f_j$ in this case the objective becomes

$$J(\alpha, f_1, \cdots , f_d) = \sum_{i=1}^N \left(y_i - \alpha - \sum_{j=1}^D f_j(x_{ij}) \right)^2 + \sum_{j=1}^D \lambda_j \int f_j^{''}(t_j)^2dt_j$$ where $\lambda_j$ is the strength of the regularizer for $f_j$
