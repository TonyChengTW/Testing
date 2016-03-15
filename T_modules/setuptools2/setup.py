from setuptools import setup, find_packages

setup(
    name = "demo1",
    version = "0.1",
    Author_email = 'tony.pig@gmail.com',
    Author = 'Tony Cheng',
    packages = find_packages('src'),
    packages_dir = {'':'src'},
    packages_data = {
        '': ['*.txt'],
        'demo': ['data/*.dat'],
    }

)
