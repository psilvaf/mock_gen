import matplotlib.pyplot as plt
import numpy as np
import healpy as hp
from astropy.io import fits
from catalog_org.read_fits_files import read_data
from catalog_org.sigmas_bins import chunks
from astropy.table import Table
import time

def mask_cut():
	pix_test=np.arange(mock_pixels['pixel'].shape[0])[np.in1d(mock_pixels['pixel'],survey_pix)]
	dec,ra=np.degrees(hp.pix2ang(nside=512, ipix=matched_pix,nest=True))

