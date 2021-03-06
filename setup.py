from setuptools import setup, find_packages


setup(name='slaccato',
      version='0.1.2',
      description='Structured Slack bot framework.',
      long_description=open('README.md').read(),
      license='MIT',
      author='Dongho Yu',
      author_email='n0rr7882@gmail.com',
      url='https://github.com/peoplefund-tech/slaccato',
      install_requires=['certifi==2018.8.24',
                        'chardet==3.0.4',
                        'idna==2.7',
                        'requests==2.19.1',
                        'six==1.11.0',
                        'slackclient==1.3.0',
                        'urllib3==1.23',
                        'websocket-client==0.53.0'],
      packages=find_packages(exclude=['slack_methods']),
      python_requires='>=3.6',
      classifiers=['Programming Language :: Python :: 3.6'])
