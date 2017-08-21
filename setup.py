#!/usr/bin/env python

from setuptools import setup


setup(
    name='libversion',
    version='0.0.1',
    description='CFFI wrapper around libversion version string comparison library',
    author='Dmitry Marakasov',
    author_email='amdmi3@amdmi3.ru',
    url='https://github.com/repology/libversion',
    license='MIT License',
    packages=['libversion'],
    setup_requires=['cffi>=1.0.0'],
    cffi_modules=['libversion/libversion_build.py:ffi'],
    install_requires=['cffi>=1.0.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ]
)
