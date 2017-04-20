from setuptools import setup, find_packages

with open('requirements.txt','r') as fp:
        requirements = [ x.strip() for x in fp ]

setup(
    name='contrail-datapipeline',
    version='0.0.1',
    url='https://github.com/alokjani/contrail-datapipeline',
    author='Alok Jani',
    author_email='Alok.Jani@ril.com',
    description='Pipeline for moving data between Contrail Analytics and On-premise collectors',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'contrail-datapipeline = contrail_datapipeline.pipeline:main',
            ]
        },
)
