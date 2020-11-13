

# R for statistics #

Slides: https://ubc-library-rc.github.io/r-stats/

## Introduction ##

### Data types ###

| Data types | Terms in R |
|--- |--- |
| Nominal, ordinal | Character (alphanumeric) or factor |
| Interval, ratio | Numeric (floating point) or integer (integer) |



### Inferrial statistics ###

1. One-sample t-test; two outcomes:
 - Fail to reject null hypothesis (no evidence to reject H0)
 - Reject null hypothesis

2. Chi-square goodnes of fit
- t-test for categorical variables
- whether the observed distribution matches the expected distribution; e.g. is gender distribution 40%-60%?
```
chisq.test( table(scores$gender), p = c(0.4,0.6)
```

| 3.  Two-sample t-test  ||
| - e.g. Do men and women have different average SAT scores? ||






## Additional Resources ##

- http://rcompanion.org/handbook/D_03.html
- https://www.statisticssolutions.com/assumptions-of-linear-regression/




## Getting started in R ##

### Setup ###

0. Fire up R Studio

1. set working directory:
```
setwd('~/rstats')
```

2. install packages
```
install.packages("psych")
install.packages("rstatix")
install.packages("dplyr")
install.packages("ggplot2")
install.packages("GGally")
```

3. Load packages
```
library(psych)
library(rstatix)
library(dplyr)
library(ggplot2)
library(GGally)
```

4. 
```
data(sat.act)
view(data)
str(scores)
```




## On Helios@CalculQuebec ##

```module load gcc/5.4.0 r/3.4.3```
