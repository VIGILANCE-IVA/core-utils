from setuptools import find_packages, setup

setup(
    name='core_utils',
    packages=find_packages(include=['core_utils']),
    version='0.1.0',
    description='Core utils',
    author='Paul Jeremiah Mugaya',
    install_requires=['numpy', 'opencv-contrib-python'],
    license='MIT',
)
