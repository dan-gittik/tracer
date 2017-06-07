import setuptools


package = dict(
    name             = 'tracer',
    version          = '0.1.0',
    author           = 'Dan Gittik',
    author_email     = 'dan.gittik@gmail.com',
    description      = 'A decorator to trace function exeuction.',
    license          = 'MIT',
    url              = 'https://github.com/dan-gittik/tracer',
    packages         = setuptools.find_packages(),
    install_requires = [
    ],
    tests_require    = [
        'pytest',
    ],
)


if __name__ == '__main__':
	setuptools.setup(**package)
