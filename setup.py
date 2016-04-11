# -*- coding: utf-8 -*-

"""
    Setup pastebin package
"""

from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="pastebin",
    version="0.0.1",
    license="MIT",

    description="dead simple pastebin",

    author="Mariusz Kozakowski",
    author_email="11mariom@gmail.com",

    url="https://mariom.pl",

    packages=find_packages(),
    include_package_data=True,

    install_requires=list(x.name for x in parse_requirements("./requirements.txt", session=False)),

    classifiers=[
        'Development Status :: 1 - Planning',

        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: MIT License',

        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    keywords=[
        'pastebin',
    ],

    entry_points={
        "console_scripts": [
            "pastebin=pastebin.pastebin:main"
        ]
    },

    test_suite='nose.collector',
    tests_require=['nose'],
)
