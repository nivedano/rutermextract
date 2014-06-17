from setuptools  import setup

VERSION = '0.1'

setup(
    name = 'rutermextract',
    packages = ['rutermextract'],

    description = 'Term extraction for Russian language',
    long_description = open('README.rst').read(),

    version = VERSION,

    author = 'Igor Shevchenko',
    author_email = 'mail@igorshevchenko.ru',
    license = 'MIT license',

    url = 'https://github.com/igor-shevchenko/rutermextract',
    download_url = 'https://github.com/igor-shevchenko/rutermextract/tarball/%s' % VERSION,

    requires = [
        'pymorphy2 (>=0.8)',
        'enum34 (>=1.0)',
    ],

    install_requires = [
        'pymorphy2 >=0.8',
        'enum34 >=1.0',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
    ],
)