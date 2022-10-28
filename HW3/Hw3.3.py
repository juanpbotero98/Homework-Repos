# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:14:02 2022

@author: dispe
"""

import numpy as np
import numpy.linalg as la
import scipy.io as sio
from os.path import dirname, join as pjoin
import matplotlib.pyplot as plt

def multiple_formatter(denominator=2, number=np.pi, latex='\pi'):
  def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
  def _multiple_formatter(x, pos):
    den = denominator
    num = np.int(np.rint(den*x/number))
    com = gcd(num,den)
    (num,den) = (int(num/com),int(den/com))
    if den==1:
      if num==0:
          return r'$0$'
      if num==1:
          return r'$%s$'%latex
      elif num==-1:
          return r'$-%s$'%latex
      else:
          return r'$%s%s$'%(num,latex)
    else:
      if num==1:
          return r'$\frac{%s}{%s}$'%(latex,den)
      elif num==-1:
          return r'$\frac{-%s}{%s}$'%(latex,den)
      else:
          return r'$\frac{%s%s}{%s}$'%(num,latex,den)
  return _multiple_formatter


class Multiple:
  def __init__(self, denominator=2, number=np.pi, latex='\pi'):
    self.denominator = denominator
    self.number = number
    self.latex = latex

  def locator(self):
    return plt.MultipleLocator(self.number / self.denominator)
  
  def formatter(self):
    return plt.FuncFormatter(multiple_formatter(self.denominator, self.number, self.latex))

#3.a

N = 64
sigma = 3.5
f0 = 10
amp_drop = 0.75
omega0 = 2*np.pi*f0/N 
n = np.arange(25)
Nrange = np.arange(N)
npolar = np.linspace(-np.pi, np.pi, N)
nfreq = np.linspace(-N/2, N/2, N)
sinusoid = np.cos(omega0*n)
# omega1 = omega0 - 0.75
omega1 = 2*np.pi*(5)/N 
# omega2 = omega0 + 0.75
omega2 = 2*np.pi*(15)/N 

gabor_filter = np.exp(-((n-13)**2)/(2*sigma**2))*sinusoid

GF_fft = np.abs((np.fft.fft(gabor_filter, N)))
GF_fft = GF_fft
GF_fft_centered = np.concatenate((GF_fft[int(N/2):], GF_fft[0:int(N/2)]))

plt.figure()
plt.plot(np.exp(-((n-13)**2)/(2*sigma**2)))
plt.title(f"Gaussian sigma = {sigma}")

plt.figure()
plt.plot(sinusoid)
plt.title(f"Sinusoid sigma = {sigma}")

plt.figure()
plt.plot(gabor_filter)
plt.title(f"Filter sigma = {sigma}")

plt.figure()
plt.plot(GF_fft)
plt.title(f"FT amp of Filter sigma = {sigma}")

plt.figure()
plt.plot(nfreq, GF_fft_centered)
plt.title(f"FT amp centered of Filter sigma = {sigma}")

plt.figure()
plt.plot(npolar, GF_fft_centered)
plt.title(f"FT amp centered of Filter sigma = {sigma}")
ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))

#Hi pass filter

#3.b
passFreq =np.abs(np.argmax(GF_fft)) 
maxAmp = np.max(GF_fft)


sinusoid0 = np.cos(omega0*Nrange)
sinusoid1 = np.cos(omega1*Nrange)
sinusoid2 = np.cos(omega2*Nrange)

convf0 = np.convolve(gabor_filter, sinusoid0)
convf1 = np.convolve(gabor_filter, sinusoid1)
convf2 = np.convolve(gabor_filter, sinusoid2)

# plt.figure()
# plt.plot(convf0)
# plt.title("convf0")
# plt.figure()
# plt.plot(convf1)
# plt.title("convf1")
# plt.figure()
# plt.plot(convf2)
# plt.title("convf2")

maxAmpf0 = np.max(convf0)
maxAmpf1 = np.max(convf1)
maxAmpf2 = np.max(convf2)
# print(maxAmpf1/maxAmpf0)
# print(maxAmpf2/maxAmpf0)

convf0_fft = np.abs((np.fft.fft(convf0, N)))
convf0_fft = convf0_fft
convf1_fft = np.abs((np.fft.fft(convf1, N)))
convf1_fft = convf1_fft
convf2_fft = np.abs((np.fft.fft(convf2, N)))
convf2_fft = convf2_fft

ampf0_fft = convf0_fft[f0]
ampf1_fft = convf1_fft[5]
ampf2_fft = convf2_fft[15]
print(ampf1_fft/ampf0_fft)
print(ampf2_fft/ampf0_fft)


convf0_fft_centered = np.concatenate((convf0_fft[int(N/2):],convf0_fft[0:int(N/2)]))
convf1_fft_centered = np.concatenate((convf1_fft[int(N/2):],convf1_fft[0:int(N/2)]))
convf2_fft_centered = np.concatenate((convf2_fft[int(N/2):],convf2_fft[0:int(N/2)]))

plt.figure()
plt.plot(nfreq, convf0_fft_centered)
plt.title("convf0_fft")
plt.figure()
plt.plot(convf0_fft)
plt.plot(f0, ampf0_fft,'r.')
plt.title("convf0_fft")

plt.figure()
plt.plot(nfreq, convf1_fft_centered)
plt.title("convf1_fft")
plt.figure()
plt.plot(convf1_fft)
plt.plot(int(np.floor(f0-amp_drop)), ampf1_fft, 'r.')
plt.title("convf1_fft")

plt.figure()
plt.plot(nfreq, convf2_fft_centered)
plt.title("convf2_fft")
plt.figure()
plt.plot(convf2_fft)
plt.plot(int(np.ceil(f0+amp_drop)), ampf2_fft,'r.')
plt.title("convf2_fft")


