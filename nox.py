# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

import nox


@nox.session
@nox.parametrize('python_version', ('2.7', '3.4', '3.5', '3.6'))
def unit_tests(session, python_version):
    session.interpreter = 'python{0}'.format(python_version)
    session.install('pytest', 'pytest-cov')
    session.install('-e', '.')
    session.run(
        'py.test',
        '--cov=duck',
        '--cov-config=.coveragerc',
        '--cov-report=term-missing',
        'tests/',
    )


@nox.session
def lint(session):
    session.install('flake8', 'flake8-import-order')
    session.run(
        'flake8',
        '--import-order-style=google',
        '--application-import-names=duck,tests',
        'duck',
        'tests',
    )
