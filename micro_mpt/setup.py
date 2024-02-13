from setuptools import setup, find_packages

setup(
    name='micro_mpt',
    version='0.1.0',
    url='https://github.com/yourusername/micro_mpt',
    author='Author Name',
    author_email='author@gmail.com',
    description='A framework for calculating microrheological properties from nanoparticle tracking data in soft matter systems',
    packages=find_packages(),    
    install_requires=['numpy', 'pandas', 'scikit-learn'],
)