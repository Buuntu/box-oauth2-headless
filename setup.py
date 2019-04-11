import setuptools 

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='box_oauth',
    version='0.3.0',
    description='Box headless OAuth2 client',
    author='Gabriel Abud',
    author_email='gabriel.jabud@gmail.com',
    zip_safe=True,
    install_requires=required,
    packages=setuptools.find_packages(),
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    tests_require=[
        'pytest'
    ],
    test_suite='pytest'
)
