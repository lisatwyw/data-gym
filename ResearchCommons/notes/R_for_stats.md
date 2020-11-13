

# R for statistics #

Date: 2020-11-13

Slides: https://ubc-library-rc.github.io/r-stats/


## Introduction ##

### Data types ###

| Data types | Terms in R |
|--- |--- |
| Nominal, ordinal | Character (alphanumeric) or factor |
| Interval, ratio | Numeric (floating point) or integer (integer) |


### Inferrial statistics ###

#### ####

1. One-sample t-test; two outcomes:
   - Fail to reject null hypothesis (no evidence to reject H0)
   - Reject null hypothesis
   
2. Chi-square goodnes of fit
   - t-test for categorical variables
   - whether the observed distribution matches the expected distribution; e.g. is gender distribution 40%-60%?
     ```chisq.test( table(scores$gender), p = c(0.4,0.6) )  # 40% for first level```
     ```levels(scores$gender)```
     
3. Two-sample t-test  (parametric; two categories)
   - e.g. Do men and women have different average SAT scores?
   
4. One-way ANOVA (more than 2 categories)
   - e.g. Do SAT scores differ by education levels?
   a. Failed to reject H0, no need to perform post-hoc
   b. If we have sign. difference to reject H0, run post-hoc such as Tukey multiple comparisons of means
   
5. Two-way ANOVA 
   - e.g. Do SAT scores differ by education levels **AND gender**?
   - should test interactions
   
6. Chi-square test of independence
   - e.g. Are education and gender dependent?   
   - ```chisq.test( table(scores$gender, scores$education))``` 
   - Null hypothesis: variables are independent
   - Alt. hypothesis: variables are not independent


#### Regression ####

1. Linear regression: ```lm```
   - Is there a linear relationship between two quantitative variables?  
   - Unlike ANOVA, at least one variable is quantitative 

   - Residual standard error:
      - F-statistics; p-value < 1e-10 means model is significant
      - multiple R-squared (shared variance y explained by model); value of 0.4 is considered significant
      
2. Multiple regression: multiple variables  
   ```
   scores %>%
   select(SATV, SATQ, ACT) %>%
   ggpairs(ggplot2::aes())
   ```
   
   

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

4. View the data frame
```
data(sat.act)
view(data)
str(scores)
```




## On Helios@CalculQuebec ##

```
module load gcc/5.4.0 r/3.4.3
install.packages('sp', repos='https://cloud.r-project.org/')
```
