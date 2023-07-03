import matplotlib.pyplot as plt
import numpy as np
import healpy as hp
from astropy.io import fits
from catalog_org.read_fits_files import read_data
from catalog_org.sigmas_bins import chunks
from astropy.table import Table
import time

def get_mock_pixels(data):
	'''
	get the pixels of the mock sample
	data: must be a fits format output, with 'RA' and 'DEC'
	return: array of pixels
	'''
	data2=data[data['DEC']>=0]
	RA=np.radians(data2['RA'])
	DEC=np.radians(data2['DEC'])
	masked_pixels=hp.ang2pix(nside=512,theta=np.radians(data2['DEC']),
	phi=np.radians(data2['RA']),nest=True)
	return masked_pixels
	

def mask_cut(mock_pixels,survey_pix,mock_data,outout_path):

	'''
	Match the full sky output from the mock sample and matches to the survey footprint.
	mock_pixel(arr): pixels from mocks nested
	survey_pix(arr): footprint nested
	z(arr): redshift
	dz_rsd(arr): redshift space distortion error
	outout_path(str): path to save file
	return: mocks for the survey fits file
	'''

	pix_test=np.arange(mock_pixels.shape[0])[np.in1d(mock_pixels,survey_pix)]

	matched_pix=mock_pixels[pix_test]
	
	dec,ra=np.degrees(hp.pix2ang(nside=512, ipix=matched_pix,nest=True))
	mock={}
	mock['RA']=ra
	mock['DEC']=dec
	mock['Z']=mock_data[pix_test]['Z_COSMO']
	mock['DZ_RSD']=mock_data[pix_test]['DZ_RSD']
	Table(mock).write(outout_path,overwrite=True)
	return dec,ra
