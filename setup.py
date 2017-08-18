# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

from setuptools import setup


# long_description = open('README.rst', 'r', encoding='utf-8').read()


setup(
    name='mock-duck',

    version='0.1.0',

    description='Easier mocking in Python.',
    # long_description=long_description,

    url='https://mock-duck.readthedocs.org',

    author='Luke Sneeringer',
    author_email='lukesneeringer@google.com',

    license='MIT License',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Topic :: Software Development :: Testing',
        'Environment :: Console',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows'
    ],

    keywords='testing automation mock stub spy',

    packages=['duck'],

    include_package_data=True,

    install_requires=(
        'six>=1.4.0,<2.0.0',
    ),
    extras_require={
        ':python_version<"3.3"': ('mock',),
    },
)
