"""setup."""
import setuptools

setuptools.setup(
    name="Jupyter Browser",
    version="0.0.1",
    url="https://github.com/rupello/jupyterbrowser",
    author="Rupert Lloyd",
    description="Browse recent notebooks inside jupyter",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords="jupyter utility",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=['ipywidgets'],
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', 'flake8>=3.3.0', 'tox>=2.7.0', 'vcrpy>=1.11.1'],
    extras_require={
        'packaging': ['setuptools>=38.6.0', 'twine>=1.11.0',],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
)
