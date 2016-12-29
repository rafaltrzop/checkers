from setuptools import setup

setup(
    name='checkers',
    version='0.0.0',
    description='Checkers game',
    url='https://github.com/rafaltrzop/checkers',
    author='Rafał Trzop',
    license='MIT',
    packages=['checkers'],
    install_requires=['flask'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
