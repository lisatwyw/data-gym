## ECG samples ##
### 1015792 ###
```
csvs=pd.read_csv('datasets/MUSE/PVC/PVCVTECGData/1015792.csv' )                 
 
for k in csvs.keys(): 
    print( '%s: \t%.2f, \t%.2f'%(k, csvs[k].min(), csvs[k].max() ) ) 
          
aVF:    -9828.62,       20602.06
aVL:    -10464.02,      7102.03
aVR:    -10825.32,      2897.53
I:      -985.80,        8067.95
II:     -8507.81,       20500.05
III:    -11199.80,      20734.70
V1:     -18379.47,      3584.25
V2:     -32047.18,      10754.97
V3:     -18498.02,      10803.56
V4:     -4477.10,       19857.40
V5:     -7479.15,       22239.63
V6:     -7578.36,       22172.90

```

### 865441 ###

```
aVF: 	-15293.88, 	24312.80
aVL: 	-11486.20, 	11118.51
aVR: 	-13763.48, 	4466.44
I: 	-2007.48, 	11873.21
II: 	-13104.08, 	24985.34
III: 	-17581.14, 	23727.78
V1: 	-12869.03, 	4556.80
V2: 	-20644.47, 	10650.73
V3: 	-6652.68, 	15556.34
V4: 	-11734.10, 	26418.60
V5: 	-12907.44, 	31465.77
V6: 	-10838.18, 	27929.16

```

## ECG attribures  ##
```
np.unique( dsets['Chinese']['Diagnostics']['Rhythm'])                                                                        
['AF', 'AFIB', 'AT', 'AVNRT', 'AVRT', 'SA', 'SAAWR', 'SB', 'SR', 'ST', 'SVT']
```


## Patient characteristics ##

```
dsets=dict() 
dsets['Chinese']=dict() 
dsets['Chinese']['AttributesDictionary']= pd.read_excel('datasets/MUSE/entire/AttributesDictionary.xlsx')
dsets['Chinese']['Diagnostics']= pd.read_excel('datasets/MUSE/entire/Diagnostics.xlsx')

dsets['Chinese2']=dict() 
dsets['Chinese2']['PVCDiagnostics']= pd.read_excel('datasets/MUSE/PVC/PVC_diagnostics.xlsx')


dsets['Chinese']['Diagnostics'].head()        

                     FileName Rhythm       Beat  PatientAge DateofBirth  Gender  VentricularRate  AtrialRate  QRSDuration  QTInterval  QTCorrected  RAxis  TAxis  QRSCount  QOnset  QOffset  TOffset
0  MUSE_20180113_171327_27000   AFIB   RBBB TWC          85  01-01-1932    MALE              117         234          114         356          496     81    -27        19     208      265      386
1  MUSE_20180112_073319_29000     SB        TWC          59  01-01-1958  FEMALE               52          52           92         432          401     76     42         8     215      261      431
2  MUSE_20180111_165520_97000     SA       NONE          20  01-01-1996  FEMALE               67          67           82         382          403     88     20        11     224      265      415
3  MUSE_20180113_121940_44000     SB       NONE          66  01-01-1951    MALE               53          53           96         456          427     34      3         9     219      267      447
4  MUSE_20180112_122850_57000     AF  STDD STTC          73  01-01-1943  FEMALE              162         162          114         252          413     68    -40        26     228      285      354

```
