from setuptools import setup, find_packages

setup(
	name='assignment0',
	version='1.0',
	author='Nishant Routray',
	author_email='nishant.routray@ufl.edu',
	packages=find_packages(exclude=('tests', 'docs', 'resources', 'tmp')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)