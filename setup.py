from setuptools import find_packages, setup

setup(
    name='my_package',
    packages=find_packages(),
    version='0.1.0',
    description='My first package',
    author='Me',
    license='MIT',
    install_requires=[
        'numpy',
        'pandas',
    ],
    author_email='pugazhm125@gmail.com',
)