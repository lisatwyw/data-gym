

# data-gym #

## Datasets ##

### Survival datasets 

#### Hospital data
- [Yale Emergency Dept dataset](YaleEDdemo.ipynb)
- [US medicare](https://data.medicare.gov/data/hospital-compare)  # external
- [EHR temporal variability](https://github.com/hms-dbmi/EHRtemporalVariability)  # external

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
- [smartphone-captured-chest-x-ray-photographs-1.0.0\Photo-MMC\MIMICCXR-photo-frontal]()
- [https://sites.duke.edu/mazurowski/resources/breast-cancer-mri-dataset/](Breast MRI, DCE sequence)

### Population statistics ###
- [COVID19 from OpenCanada](datasets/OpenCanada_COVID19.ipynb)






## Demo Python ##

### General ###

#### Data I/O ####

- [Extracting data: background color of cells in Excel files](demo/parsing_excel.md)
- [Reading in data from Google spreadsheet](demo/gsheet_demo.ipynb)
  - [Example 2: Subject999](demo/Prophet_Subject999.ipynb)
- [Converting from PDF using batch mode](misc/pdf.md)

#### Plotting ####  
- [Creating subplots](demo/subplots.ipynb)
- [Correlogram with numbers](demo/correlogram_in_python.ipynb)
- [Example of plotting in 3D](demo/WISDM_LSTM.ipynb)

#### Prelim. analyses ####  

- [Discretize variables using numpy.matlib.repmat](demo/discretize.ipynb)
- [Data visualization via dimensionality-reduction](demo/dimRedux.ipynb)
- [Explore some ONC datasets](demo/data_playground.ipynb)
- [Explore the YaleED dataset](YaleEDdemo.ipynb)
- [Explore clinical codes; calculate some clinical indices](demo/clinical_codes.ipynb)

#### Preprocessing ####

- [biosppy](demo/biosppy.ipynb) 

#### Training models ####
- [Logistric regresssion and LSTM using PIMA](demo/LR_vs_LSTM_on_PIMA_without_skin.ipynb)
- [LR and MLP using PIMA](demo/LR_vs_LSTM_vs_MLP_on_PIMA.ipynb)
- Time-series classification (WISDM dataset)
    - [MLP](demo/WISDM.ipynb)
    - [LSTM, GRU](WISDM_lstm.ipynb)
    - [1D-CNN](WISDM_1dcnn.ipynb)

#### Misc. ####

- [Improving reproducibility with seeds](demo/random_seeding.md)

### Common code snippets ###

- [Jupyter-oriented](misc/code_snippets.md)


## Helpful links ##

- [Start R notebook](https://colab.research.google.com/notebook#create=true&language=r)
- [Getting started with R by me](demo/R_get_started.ipynb)

## Resources ##

### Visual analytics ###

- ["Making Data Visual" by Danyel Fisher, Miriah Meyer](https://makingdatavisual.github.io/)
   - [How to choose?](https://makingdatavisual.github.io/figurelist.html)
- [Visualizing missing data quickly](https://github.com/ResidentMario/missingno)
- [Visualization: bad examples](https://viz.wtf/)
- [Violinplot via Seaborn](http://seaborn.pydata.org/examples/wide_form_violinplot.html)
- [Cartograms (explained in first ten seconds)](https://www.youtube.com/watch?v=q76QLy9Dqs0&feature=youtu.be)

### Statistics & cross-validation ###

- ["Statistical Approaches to the Model Comparison Task in Learning Analytics," Gardner & Brooks, LAK2017](http://ceur-ws.org/Vol-1915/paper2.pdf)
- [slides by B Evans](https://ecs.wgtn.ac.nz/foswiki/pub/Groups/ECRG/StatsGuide/Significance%20Testing%20for%20Classification.pdf)
- Notes: "[...] ordinal regression is known to perform better than softmax on ordinal data (Cheng et al., 2008)"

### Meta-data ###

- [BioLinCC](https://biolincc.nhlbi.nih.gov/studies/?s=rank&not_initial=Yes&q=acute+care+&d=name&d=acronym&d=available_resources&d=period&page_size=500&so=name&so=acronym&so=available_resources&so=period)
- [DataOne](https://www.dataone.org/investigator-toolkit)
- [DataOne search interface ](https://search.dataone.org/data)



                     
