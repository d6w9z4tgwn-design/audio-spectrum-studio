import argparse,numpy as np
from pathlib import Path
from scipy.io import wavfile

def spectrum(samples,rate):
    x=np.asarray(samples,dtype=float)
    if x.ndim==2: x=x.mean(axis=1)
    if len(x)<2: raise ValueError('Audio too short')
    x=x-x.mean();w=np.hanning(len(x));return np.fft.rfftfreq(len(x),1/rate),np.abs(np.fft.rfft(x*w))
def main():
    p=argparse.ArgumentParser(description='Create a frequency spectrum image from a WAV file.');p.add_argument('input');p.add_argument('output');p.add_argument('--max-frequency',type=float,default=None,help='Limit chart to this frequency in Hz.');a=p.parse_args();rate,x=wavfile.read(a.input);f,y=spectrum(x,rate)
    if a.max_frequency is not None and not 0<a.max_frequency<=rate/2: p.error('--max-frequency must be between 0 and the Nyquist frequency')
    import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
    db=20*np.log10(np.maximum(y/max(y.max(),1e-12),1e-12));plt.style.use('seaborn-v0_8-whitegrid');fig,ax=plt.subplots(figsize=(11,5.5));ax.plot(f,db,color='#4f46e5',linewidth=1.2);ax.set(xlabel='Frequency (Hz)',ylabel='Relative amplitude (dB)',title=f'Audio spectrum — {Path(a.input).name}',ylim=(-100,3));ax.set_xlim(0,a.max_frequency or rate/2);ax.spines[['top','right']].set_visible(False);fig.tight_layout();Path(a.output).parent.mkdir(parents=True,exist_ok=True);fig.savefig(a.output,dpi=180);plt.close(fig)
if __name__=='__main__': main()
