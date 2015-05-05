import os
from setuptools import setup, find_packages

import myblog

setup(
    name='myblog',
    version=myblog.__version__,
    description='',
    long_description=open(os.path.join('README.rst')).read(),
    author=myblog.__author__,
    author_email=myblog.__email__,
    url=myblog.__url__,
    scripts=['bin/myblog'],
    packages=find_packages(),
    keywords='django, zinnia, blog',
    classifiers=[
        'Framework :: Django',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license=myblog.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=open('requirements.txt').read().splitlines()
)
