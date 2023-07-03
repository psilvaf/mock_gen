from setuptools import setup
import os

setup(name='mock_gen',
	version='0.1.0',
   	author='Paula Ferreira',
   	author_email='psilf12@gmail.com',
   	packages=['mock_gen',],
   	#scripts=['bin/script1','bin/script2'],
   	#url='http://pypi.python.org/pypi/PackageName/',
   	license='LICENSE.txt',
   	description='An awesome package that does something',
  	#long_description=open('README.txt').read(),
  	install_requires=[
	"astropy",
	"numpy",
	'scipy',
	'pandas',
	'colossus',],)
