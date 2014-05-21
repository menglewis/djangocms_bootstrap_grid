#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cmsplugin_bootstrap_grid

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = cmsplugin_bootstrap_grid.__version__

setup(
    name='djangocms-bootstrap-grid',
    version=version,
    description='Collection of plugins for DjangoCMS to create a Bootstrap 3 Responsive Grid',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='David Lewis',
    author_email='meng.lewis@gmail.com',
    url='https://github.com/menglewis/djangocms_bootstrap_grid',
    packages=['cmsplugin_bootstrap_grid'],
    include_package_data=True,
    install_requires=['Django-CMS>=3.0'],
    license='BSD',
    zip_safe=False,
    keywords='djangocms-bootstrap-grid',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
)
