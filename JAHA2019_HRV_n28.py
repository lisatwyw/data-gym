
# download xls, deidentified ECG patch HRV dataset, n=28    
! wget -O PACE.xls https://github.com/Tereshchenkolab/HRV/blob/master/PACE%20deidentified%20ECGpatch%20HRV%20dataset%2028pts.xls
    
# xls contains: 
#'hour', 'min', 'phase_dialysis', 'SVT', 'VT', 'Afib', 'pause', 'meanrrms', 'rmssdms', 'LF_power', 'HF_power', 'LF_HF_ratio', 'sample_entropy', 'renyi_entropy', 'SD1', 'SD3', 'SD12', 'heart_rate']

import pandas as pd
df=pd.read_excel('data/JAHA2019/PACE.xls')     
 
for d in range(1,29):    
    q=np.where( df['id']==d )[0]    
    plt.clf(); 
    
    H=24 # width, if subplot
    W=28 # height, if subplots
    
    nplts=8    
    fig,ax=plt.subplots(nplts,1, figsize=( H, W ))
    try:
        sess.SMALL_SIZE = H*.8
        sess.MEDIUM_SIZE = H*1.5
        sess.BIGGER_SIZE = H*2    
        myutils.update_font_sizes( sess )
    except:
        pass

    p=df['phase_dialysis'][q]
    pause=df['pause'][q]
    afib=df['Afib'][q]
    svt=df['SVT'][q]
    vt=df['VT'][q]
    
    x = (df['hour'][q]*60 + df['min'][q] )/60               
    hr24 = df['hr24'][q]    
    
    a=0
    ax[a].plot( x,p,label='Phase of dialysis')    
    ax[a].plot( x,pause,label='Pause')
    ax[a].plot( x,afib,label='AFib')
    ax[a].plot( x,svt,label='SVT')
    ax[a].plot( x,vt,label='VT')
    ax[a].plot( x,hr24/24*6,label='cycle',color=[.5,.5,.5], linestyle='dotted')
    ax[a].set_title('States')
    ax[a].legend()    
    
    a=1 
    ax[a].plot( x, df['rmssdms'][q],label='rMSSD (ms)')
    ax[a].set_title('Indices of parasympathetic tone balance')    
    ax[a].legend()

    a=2
    ax[a].plot( x, df['SD1'][q],label='SD1'.upper())
    ax[a].plot( x, df['HF_power'][q],label='High frequency power')    
    ax[a].legend()

    a=3
    ax[a].plot( x, df['SD3'][q],label='SD2'.upper())
    ax[a].set_title('Indices of sympathovagal balance')    
    ax[a].legend()

    a=4    
    ax[a].plot( x, df['LF_HF_ratio'][q],label='ratio')        
    ax[a].plot( x, df['SD12'][q],label='SD12')        
    ax[a].legend()
    
    a=5
    ax[a].plot( x, df['LF_power'][q],label='Low frequency power')
    ax[a].plot( x, df['heart_rate'][q],label='Heart rate (bpm)')   
    ax[a].set_title('Frequency- and Time- domain measures')    
    ax[a].legend()

    a=6
    ax[a].plot( x, df['meanrrms'][q],label='Mean RRMS')    
    ax[a].legend()
    
    a=7
    ax[a].plot( x, df['renyi_entropy'][q],label='Renyi')
    ax[a].plot( x, df['sample_entropy'][q],label='Entropy')
    ax[a].set_title('Nonlinear HRV measures (fluct. on short-term N-N)')        
    ax[a].legend()
    ax[a].set_xlabel('Time')
        
    plt.suptitle('ID%02d.png'% d)
    plt.tight_layout()
    plt.savefig('data/JAHA2019/JAHA2019_ID%02d.png'% d)                                                                                                   
