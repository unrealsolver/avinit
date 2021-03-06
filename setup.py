#!/usr/bin/env python

from distutils.core import setup

setup(
    name='avinit',
    version='1.2.2',
    description='Generate avatars using name initials',
    author='Sergio Oliveira',
    author_email='seocam@seocam.com',
    url='https://github.com/CraveFood/avinit',
    packages=['avinit'],
    extras_require={
        'png': ['CairoSVG>=1.0,<2.0.0', 'cairocffi<1.0.2']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
    ],
)
