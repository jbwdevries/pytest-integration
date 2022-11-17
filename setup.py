from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pytest_integration',
    version='0.2.3',
    author='Johan B.W. de Vries',
    description='Organizing pytests by integration or not',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jbwdevries/pytest-integration',
    project_urls={
        'Bug Tracker': 'https://github.com/jbwdevries/pytest-integration/issues',
        'Source Code': 'https://github.com/jbwdevries/pytest-integration',
    },
    packages=['pytest_integration'],
    # the following makes a plugin available to pytest
    entry_points={
        'pytest11': ['pytest_integration = pytest_integration.pytest_plugin'],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Framework :: Pytest',
    ],
    python_requires='>=3.6',
    setup_requires=[
        'wheel',
    ],
)
