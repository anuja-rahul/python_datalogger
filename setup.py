from setuptools import setup, find_packages
import pathlib


VERSION = '0.0.4'
DESCRIPTION = 'Simplified data logger for Python'
LONG_DESCRIPTION = pathlib.Path("README.md").read_text()
LICENSE = 'MIT License'

# Setting up
setup(
    name="python_datalogger",
    version=VERSION,
    author="Anuja Rahul Gunasinghe",
    author_email="<a.r.gunasinghe@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    project_urls={
        "Source": "https://github.com/anuja-rahul/python_datalogger",
        "Documentation": "https://github.com/anuja-rahul/python_datalogger/blob/master/README.md"
    },
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    keywords=['python', 'DataLogger', 'logger', 'timeit', 'log_debug', 'log_info', 'log_warning', 'log_error', 'log_critical'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education :: Testing",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.10',
    include_package_data=True,
)
