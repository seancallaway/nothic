from setuptools import setup

setup(
    name='nothic',
    version='0.1.0',
    py_modules=['nothic'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'nothic = nothic.__main__:main',
        ],
    },
)
