from setuptools import setup


setup(name='dataservices',
      version='11.1',
      packages=['dataservices', 'dataservices.utils'],
      description='Python interface for querying webservices data',
      license='MIT',
      url='https://github.com/MicroStrategy/dataservices',
      author=[
          'Jeff Maddocks'
      ],
      author_email=[
          'jmaddocks@microstrategy.com'
      ],
      install_requires=[
          'pandas',
          'xlrd',
          'datetime'
      ]
      )