from distutils.core import setup

setup(
    name='CryptoAnalysis',
    version='0.1.0',
    author='Ashuthosh Gowda',
    author_email='a4gowda@gmail.com',
    packages=['crypto_analysis'],
    #scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    #url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Useful stuff.',
    long_description=open('README.txt').read(),
    install_requires=[
        "sklearn",
        "pandas",
    ],
)
