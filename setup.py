from setuptools import setup

setup(
    name='zomatoapi',
    version='1.0.1',
    url='https://github.com/gaurav19063/zomatoapi',
    description='A simple python wrapper for the Zomato API',
    author='Gaurav Lodhi',
    author_profile='https://github.com/gaurav19063',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='Zomato',
    install_requires=[
        'requests==2.11.1'
    ]
)
