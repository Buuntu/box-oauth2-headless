from setuptools import setup

setup(
    name='box_oauth',
    version='0.1.0',
    description='Box headless OAuth2 client',
    url='http://github.com/Buuntu/box-oauth2',
    author='Gabriel Abud',
    author_email='gabriel.jabud@gmail.com',
    zip_safe=True,
    install_requires=[
        'selenium',
        'geckodriver',
        'boxsdk',
        'keyring'
    ],
    tests_require=[
        'pytest'
    ],
    test_suite='pytest'
)
