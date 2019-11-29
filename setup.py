from setuptools import setup

setup(
    name='pytest_integration',
    packages=['pytest_integration'],
    # the following makes a plugin available to pytest
    entry_points={
        'pytest11': ['name_of_plugin = pytest_integration.pytest_plugin'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Pytest',
    ],
    setup_requires=[
        'wheel',
    ],
)
