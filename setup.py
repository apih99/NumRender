from setuptools import setup, find_packages

setup(
    name='numword',
    version='0.1.0',
    author='Shahrul Hafiz', 
    author_email='hafizcr716@gmail.com', 
    description='A library to convert numbers to words and vice versa',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/apih99/numword', 
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License ::  MIT License', 
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
  