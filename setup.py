from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='mss',
    version='1.0',
    author='Felipe Cabrera',       
    author_email='me@felieppe.com',
    description='A Python-based movie seat reservation simulator', 
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/felieppe/movie-seats-simulator',
    packages=find_packages(where='.'),      
    classifiers=[                  
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mss = src.main:main'
        ]
    }
)