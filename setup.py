from distutils.core import setup

with open('README.txt') as file:
    long_description = file.read()

setup(name='rpstool',
      version='1.0',
      description='Access log requests per second counter',
      long_description=long_description,
      author='yagb',
      author_email='ok@yagb.ru',
      url='https://github.com/yagb/rpstool',
      scripts=['rpstool'])
