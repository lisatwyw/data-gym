

# R for statistics #

Slides: https://ubc-library-rc.github.io/r-stats/

## Resources ##

- rcompanion.org/handbook/D_03.html
- https://www.statisticssolutions.com/assumptions-of-linear-regression/


## Data types ##

| Data types | Terms in R |
|--- |--- |
| Nominal, ordinal | Character (alphanumeric) or factor |
| Interval, ratio | Numeric (floating point) or integer (integer) |



## Inferrial statistics ##


## Getting started ##

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
