from distutils.core import setup

setup(
    name='ModemStatus',
    version='0.0.01',
    packages=['ModemStatus'],
    url='https://github.com/codytrey/ModemStatus',
    license='GNU GPLv3',
    author='Cody Belcher',
    author_email='cody.t.belcher@gmail.com',
    description='Python package to query cable modem status information and log results to an sqlite database',
    include_package_data=True
)
