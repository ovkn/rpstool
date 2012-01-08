from distutils.core import setup

with open('README.txt') as file:
    long_description = file.read()

setup(name='rpstool',
      version='1.0',
      description='A simple requests per second (rps) counter',
      long_description=long_description,
      author='OVK',
      author_email='me@ovk.name',
      url='https://github.com/ovkn/rpstool',
      scripts=['rpstool'])
