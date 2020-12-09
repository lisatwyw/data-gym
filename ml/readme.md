# Ensemble methods 

## Random forest
## Gradient boosting algorithms

### Concepts recapped:

- Boosting: iteratively trains a sequence of weak learners 
  - At each iteration, training examples are weighted accordingly to the success of the learners learnt at the previous iteration 
- AdaBoost equivalent to minimizing exponential loss function
- Gradient boosting minimizes arbitrary loss functions; fits next weak learner by performing regression on a function of the gradient vector of the loss evaluated at the previous iteration
- Below packages use decision trees as base learner 

[Light GBM in Python](https://lightgbm.readthedocs.io/)

[XGboost in Python](https://xgboost.readthedocs.io/en/latest/python/python_intro.html)
- gb-tree, gb-linear, dart
- SHAPly for interpretability

[CatBoost in Python](https://towardsdatascience.com/why-you-should-learn-catboost-now-390fb3895f76)
- Pros: 
  - SHAPly for interpretability
  - missing values of numeric variables are okay
  - Text processing
  - GPU processing
- Caveats: missing values of categorical variables need to be filled

### [Comparisons of XGBoost, CatBoost, and LightGBM presented at NeurIPS 2018](https://arxiv.org/pdf/1809.04559.pdf)

#### Findings:
- CatBoost converged to good solution 
- XGBoost cannot run when feature set gets too large
- Largest runtime reduction in XGBoost when GPU is used over CPU 
- LightGBM may converged to better solutions 

#### Evaluation on four datasets

|           | # of train + val samples | # of features | Sparsity of training | Task        | Metric |  XGBoost** | LightGBM** | Catboost** |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Higgs     | 10,500,000+500,000     | 28            | 0.0789               | binary      | AUC-ROC | 0.84 | 0.86^ | 0.85 |
| Epsilon   | 400,000+100,000        | 2,000         | 0                    | binary      | AUC-ROC | n/a | 0.95 | 0.95^ |
| Microsoft | 723,412+241,521        | 136           | 0.0789               | 5-class     | NDCG*   |0.49^ | 0.49  |  0.38 |
| Yahoo     | 473,134+165,660        |  699          | 0.0789               | 5-class     | NDCG    |0.798^ | 0.797 | 0.74 |

*NDCG: Normalized discounted cumulative gain

**Performance metric evaluated on test set


#### Parameters compared: 
![From https://towardsdatascience.com/catboost-vs-light-gbm-vs-xgboost-5f93620723db](https://miro.medium.com/max/1000/1*A0b_ahXOrrijazzJengwYw.png)
