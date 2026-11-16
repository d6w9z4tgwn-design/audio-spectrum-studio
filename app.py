import argparse,numpy as np
from scipy.io import wavfile

def spectrum(samples,rate):
    x=np.asarray(samples,dtype=float)
    if x.ndim==2: x=x.mean(axis=1)
    if len(x)<2: raise ValueError('Audio too short')
    x=x-x.mean();w=np.hanning(len(x));return np.fft.rfftfreq(len(x),1/rate),np.abs(np.fft.rfft(x*w))
def main():
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');a=p.parse_args();rate,x=wavfile.read(a.input);f,y=spectrum(x,rate)
    import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
    plt.plot(f,20*np.log10(np.maximum(y/max(y.max(),1e-12),1e-12)));plt.xlabel('Frequency (Hz)');plt.ylabel('Relative amplitude (dB)');plt.tight_layout();plt.savefig(a.output)
if __name__=='__main__': main()
