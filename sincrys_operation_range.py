import os, h5py
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12})
plt.rcParams.update({'font.family': 'sans-serif',})
fig, ax = plt.subplots(1, 1, figsize=(18/2.54, 14/2.54), sharex=True, sharey=True)
#
# Experimental Flux Scan
# with h5py.File(os.path.join(os.path.split(__file__)[0], 'scan-5205.h5')) as h5f:
#     steps_y, steps_x = np.array(h5f['entry/title'][()].decode('utf-8').split())[[4,8]]
#     steps_x = int(steps_x) + 1
#     steps_y = int(steps_y) + 1
#     nrg_exp = (h5f['/entry/instrument/hdcm_energy/value'][:]).reshape(steps_x, steps_y)
#     gap_exp = (h5f['/entry/instrument/IVU_R3_304_GAP/value'][:]).reshape(steps_x, steps_y)
#     flx_exp = (h5f['/entry/instrument/albaem-bpm_ch1/data'][:]).reshape(steps_x, steps_y)
#im = ax.pcolormesh(gap_exp, nrg_exp, flx_exp, cmap='bone_r')
#
# IVU data
ivu_data = np.load(os.path.join(os.path.split(__file__)[0], 'ivu_k_scan.npy'))
nrg_ivu = ivu_data['energy'].astype(float)
gap_ivu = ivu_data['gap'].astype(float)
flx_ivu = ivu_data['flux'].astype(float)
im = ax.pcolormesh(gap_ivu, nrg_ivu, flx_ivu, cmap='bone_r', vmin=1e11, vmax=1.0e14)
# Overlay
#axs[1].pcolormesh(gap_exp, nrg_exp, flx_exp, cmap='bone_r')
#axs[1].pcolormesh(gap_ivu, nrg_ivu, flx_ivu, cmap='bone_r', vmin=1e11, vmax=1.5e14, alpha=.5)
cbar = fig.colorbar(im, label=r'Intensity [ph/s/0.1%]')
#Labels
ax.set_title('IVU Harmonics / SinCrys Operation Range')
ax.set(ylabel='Energy [keV]')
ax.set(xlabel='Gap [mm]')
# Limits
ax.set_xlim(4.4, 6.0)
ax.set_ylim(15, 35)
# Ticks
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(MultipleLocator(1))
# Grid
ax.grid(visible=True, which='major', color='gray', linestyle='-', alpha=0.5)
ax.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.1)
# Annotations
# Harmonics
ax.annotate( '$5^{th}$', xy=(5.9,16.5), color='gray', alpha=0.5)
ax.annotate( '$6^{th}$', xy=(5.9,19.5), color='gray', alpha=0.5)
ax.annotate( '$7^{th}$', xy=(5.9,22.5), color='gray', alpha=0.5)
ax.annotate( '$8^{th}$', xy=(5.9,26.0), color='gray', alpha=0.5)
ax.annotate( '$9^{th}$', xy=(5.9,29.0), color='gray', alpha=0.5)
ax.annotate('$10^{th}$', xy=(5.8,32.0), color='gray', alpha=0.5)
ax.annotate('$11^{th}$', xy=(5.6,34.0), color='gray', alpha=0.5)
ax.annotate('$12^{th}$', xy=(5.2,34.0), color='gray', alpha=0.5)
ax.annotate('$13^{th}$', xy=(4.9,34.0), color='gray', alpha=0.5)
ax.annotate('$14^{th}$', xy=(4.6,34.0), color='gray', alpha=0.5)
# SinCrys
#ax.annotate('SinCrys', xy=(-0.03, 0.26), xycoords='axes fraction', rotation=90, size=12, weight='medium', color='gray')
#ax.annotate('SinCrys', xy=(0.006, 0.26), xycoords='axes fraction', rotation=90, size=13, weight='medium', color='gray')
#ax.annotate('SinCrys', xy=(4.6,20.2), rotation=22, size=14, weight='medium', color='gray')
ax.annotate('SinCrys', xy=(4.4,20.9), rotation=22, size=14, weight='medium', color='gray')
ax.annotate( '9', xy=(4.7,20.0), color='gray', size=65, weight='bold', alpha=0.10)
ax.annotate( '8', xy=(5.2,20.0), color='gray', size=65, weight='bold', alpha=0.10)
ax.annotate( '7', xy=(5.7,20.0), color='gray', size=65, weight='bold', alpha=0.10)
# Rectangles
#ax.add_artist(Rectangle((4.5,20), 1.5, 3.0, facecolor='None', edgecolor='gray', alpha=0.30))
ax.add_artist(Rectangle((4.4,20), 0.5, 3.0, facecolor='gray', edgecolor='None', alpha=0.30))
ax.add_artist(Rectangle((4.9,20), 0.5, 3.0, facecolor='gray', edgecolor='None', alpha=0.20))
ax.add_artist(Rectangle((5.4,20), 0.6, 3.0, facecolor='gray', edgecolor='None', alpha=0.10))

plt.tight_layout()
fig.savefig(os.path.join(os.path.split(__file__)[0], 'sincrys_operation_range.png'), dpi=600)
plt.show()
