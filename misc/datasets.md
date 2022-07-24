
## Datasets ##

### Survival datasets 

#### Hospital data
- [Yale Emergency Dept dataset](YaleEDdemo.ipynb)
- [US medicare](https://data.medicare.gov/data/hospital-compare)  # external
- [EHR temporal variability](https://github.com/hms-dbmi/EHRtemporalVariability)  # external
- [NHANES](https://wwwn.cdc.gov/nchs/nhanes/nhefs/#dfd)
- [subset of SEER](https://ieee-dataport.org/open-access/seer-breast-cancer-data) 
  - 4024 samples, 16 vars in total 
  - Time2event: ```Survival Months```, ```Status``` (```Dead``` vs ```Alive```)

#### ICU datasets
- [HiRID 2020]
- [WIDS2020 (on Kaggle)]
- [ICU: septic shock alert (Liu et al., Scientific Reports 2019)](https://github.com/instigatorofawe/shockalert-documented) # external
- [COVID2019](https://github.com/beoutbreakprepared/nCoV2019)
  - time2event, event = {discharge, death}

#### Various
- [ESP (Early Stage Prediction) for Longitudinal Data](https://github.com/MLSurvival/ESP)


### ECG ###
- [ECG-ViEW](demo/ECG_ViEW.ipynb)
- [PTB](demo/PTB.ipynb)
- [Various on PhysioNet](https://physionet.org/content/?topic=atrial)

### Physiological time-series ###

- [HRV data (JAHA2019)](demo/JAHA2019_HRV_n28.py)
- [Subject999](demo/Prophet_Subject999.ipynb)
- [Fitbit data from 18 subjects](demo/Fitbit.ipynb)
- [WISDM dataset](demo/WISDM.ipynb)
- [eDREAM, 2016](http://www.dsp.utoronto.ca/projects/eDREAM/)
  ``` 
  - Wireless electroencephalogram (EEG) headband
  - Electrocardiography (ECG), Galvanic Skin Responses (GSR) sensors and a respiration band
  - Remote eye-tracker
  - Participant-facing video-racordings
  - Participant-facing color cameras (the non-identifiable portion of the dataset can be available for research purposes.)
  ```
- SWELL, WESAD
- Contactless cardiac arrest detection using smart devices, 2020:
  ```All data necessary for interpreting the manuscript have been included. The datasets used in the current study are not publicly available due to the sensitivity of 9-1-1 calls but are available from the corresponding authors on reasonable request and with the permission of Public Health-Seattle & King County, Division of Emergency Medical Services.```
  - Sample wave file (1.21GB) in [their published code](https://cardiacalert.cs.washington.edu/)

### Medication 
- http://dataset.lixoft.com/data-set-examples/

  
### Older datasets ###
- [Right heart catheterization dataset](http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/rhc.html)
- [Diabetes](demo/LR_vs_LSTM_on_PIMA_without_skin.ipynb)
- [National longitudinal mortality survey](https://www.census.gov/topics/research/nlms.Project_Overview.html) # turnaround time maybe within 24 hours

### Imaging data ###
- [smartphone-captured-chest-x-ray-photographs-1.0.0\Photo-MMC\MIMICCXR-photo-frontal](https://physionet.org/content/cxr-phone/1.0.0/)
- [Breast MRI, DCE sequence](https://sites.duke.edu/mazurowski/resources/breast-cancer-mri-dataset/)

### Population statistics ###
- [COVID19 from OpenCanada](datasets/OpenCanada_COVID19.ipynb)



