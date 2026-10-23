from setuptools import find_packages
from setuptools import setup

import sys


version = '0.7.1.dev0'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name='imio.dataexchange.core',
    version=version,
    description="Data exchange classes for imio webservice",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Imio data exchange',
    author='IMIO',
    author_email='support@imio.be',
    url='https://github.com/imio/',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # Python 3: the namespace __init__.py extends __path__ itself, a -nspkg.pth
    # would hide the PEP 420 portions of imio.amqp and imio.dataexchange.db
    namespace_packages=(
        ['imio', 'imio.dataexchange'] if sys.version_info[0] == 2 else []
    ),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={
        'script': [
            'imio.amqp',
            'imio.dataexchange.db',
        ],
    },
    entry_points="""
    [console_scripts]
    incomingmail_dispatcher = imio.dataexchange.core.scripts.incomingmaildispatcher:main
    outgoingmail_dispatcher = imio.dataexchange.core.scripts.outgoingmaildispatcher:main
    outgoinggeneratedmail_dispatcher = imio.dataexchange.core.scripts.outgoinggeneratedmaildispatcher:main
    deliberation_dispatcher = imio.dataexchange.core.scripts.deliberationdispatcher:main
    incoming_email_dispatcher = imio.dataexchange.core.scripts.incomingemaildispatcher:main
    """,
)
