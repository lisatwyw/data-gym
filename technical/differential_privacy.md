
# Differential privacy

"For all datasets D1 and D2 that differ on a single element, and for all subsets S of the function
image of the randomized algorithm A:

P(A(D1) ∈ S) ≤ e^epsilon P(A(D2) ∈ S)
the probability distribution differences between all possible D1 and D2 for all subsets of the function image of the randomized
algorithm should be less than e^epsilon

## Direct identifiers

obviously identifiable data, include full names, or
specific uniquely identifiable numbers assigned to individuals

e.g. 
- social security number, driving license number, PHN, etc
- less obvious: hospital number (dependent on country?)

## Indirect identifiers

e.g. date of birth, initials, phone numbers, and postcodes

### Potentially identifiable information

"information that in the presence of additional data may allow for re-identification of an individual"

e.g. dates of medical procedures or visits, rare conditions, etc. 

### Non-identifiable information 

e.g. laboratory and physiology test results, clinical coding, etc.



## Refs

https://onlinelibrary.wiley.com/doi/epdf/10.1002/spe.2812

https://anomagram.fastforwardlabs.com/
