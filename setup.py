from distutils.core import setup

setup(
    name='ModemStatus',
    version='0.0.02',
    packages=['ModemStatus'],
    install_requires=[
        'bs4',
        'requests',
    ],
    url='https://github.com/codytrey/ModemStatus',
    license='GNU GPLv3',
    author='Cody Belcher',
    author_email='cody.t.belcher@gmail.com',
    description='Python package to query cable modem status information and log results to an sqlite database',
    include_package_data=True
)
