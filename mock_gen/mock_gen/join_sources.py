import matplotlib.pyplot as plt
import numpy as np
import healpy as hp
from astropy.io import fits
from catalog_org.read_fits_files import read_data
from catalog_org.sigmas_bins import chunks
from astropy.table import Table
import time

def join_mock()
mock=[read_data('mocks/'+str(i)+'.fits') for i in range(50)]
