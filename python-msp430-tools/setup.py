# This is a setup script for pythons distutils. It will install the
# python-msp430-tools extension when run as: python setup.py install

# Author: Chris Liechti <cliechti@gmx.net>
#
# This is open source software under the BSD license. See LICENSE.txt for more
# details.


from distutils.core import setup
import sys
import glob

setup(
    name="python-msp430-tools",
    description="Python MSP430 Tools",
    version="0.6",
    author="Chris Liechti",
    author_email="cliechti@gmx.net",
    url="http://launchpad.net/python-msp430-tools/",
    packages=[
            'msp430',
            'msp430.asm',
            'msp430.bsl',
            'msp430.bsl.target',
            'msp430.bsl5',
            'msp430.gdb',
            'msp430.jtag',
            'msp430.legacy',
            'msp430.listing',
            'msp430.memory',
            'msp430.shell',
            ],
    package_dir={'msp430': 'msp430'},
    package_data={'msp430': [
            'asm/definitions/msp430-mcu-list.txt',
            'bsl/BL_150S_14x.txt',
            'bsl/BL_150S_44x.txt',
            'bsl/BS_150S_14x.txt',
            'bsl/patch.txt',
            'bsl5/RAM_BSL_00.08.08.39.txt',
            ]},
    scripts=[
            'scripts/msp430-bsl.py',
            'scripts/msp430-bsl-legacy.py',
            'scripts/msp430-bsl-fcdprog.py',
            'scripts/msp430-bsl-telosb.py',
            'scripts/msp430-compare.py',
            'scripts/msp430-convert.py',
            'scripts/msp430-downloader.py',
            'scripts/msp430-gdb.py',
            'scripts/msp430-generate.py',
            'scripts/msp430-hexdump.py',
            'scripts/msp430-jtag-legacy.py',
            'scripts/msp430-jtag.py',
            'scripts/msp430-ram-usage.py',
            'scripts/msp430-tool.py',
            ],
    license="Simplified BSD License",
    long_description=open('README.txt').read(),
    classifiers = [
#        'Development Status :: 5 - Production/Stable',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Software Development :: Assemblers',
        'Topic :: Software Development :: Libraries',
    ],
)
