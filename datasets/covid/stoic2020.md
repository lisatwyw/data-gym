
# STOIC

[https://pubs.rsna.org/doi/10.1148/radiol.2021210384](STOIC2020) Challenge data on CT for predicting 1-month outcomes and COVID19 positivity

- [https://pubs.rsna.org/doi/suppl/10.1148/radiol.2021210384/suppl_file/ry210384suppa1.pdf](supp)

## Getting Started

### Download the file on labels

```
aws s3 cp s3://stoic2021-training/metadata/ . --recursive --no-sign-request
```

### ```download.sh```

Script to download in background mode:

```
#!/bin/bash
aws s3 sync s3://stoic2021-training/ . --no-sign-request
```

```nohup download.sh &```


## Relevant works 

- [GLCM](https://www.inderscienceonline.com/doi/abs/10.1504/IJCAT.2021.117275)
- [RSF](https://github.com/robinwang08/COVID19/blob/master/RSF_DL_Clin_Top_Slice_Share.py)

