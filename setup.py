from setuptools import setup
setup(
    name = 'ipsum',
    version = '0.1.0',
    packages = ['ipsum'],
    entry_points = {
        'console_scripts': [
            'ipsum = ipsum.__main__:main'
        ]
    })