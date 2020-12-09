### Boosted trees

[Comparison of XGBoost, CatBoost, and LightGBM presented at NeurIPS 2018](https://arxiv.org/pdf/1809.04559.pdf)
- used four datasets:

|           | # of train + val samples | # of features | Sparsity of training | Task        | Metric |
|-----|-----|-----|-----|-----|-----|
| Higgs     | 10,500,000 + 500,000     | 28            | 0.0789               | binary      | AUC-ROC |
| Epsilon   | 400,000 + 100,000        | 2,000         | 0                    | binary      | AUC-ROC |
| Microsoft | 723,412 + 241,521        | 136           | 0.0789               | 5-class     | Normalized discounted cumulative gain |
| Yahoo     | 473,134 + 165,660        |  699          | 0.0789               | 5-class     | Normalized discounted cumulative gain |

[XGboost]

[CatBoost with SHAPly for interpretability](https://towardsdatascience.com/why-you-should-learn-catboost-now-390fb3895f76)
- Pros: 
  - missing values of numeric variables are okay
  - Text processing
  - GPU processing
- Caveats: missing values of categorical variables need to be filled
