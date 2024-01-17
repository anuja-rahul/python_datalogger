from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Simplified data logger for Python'
LONG_DESCRIPTION = 'A package that allows to log data and errors faster and easily'

# Setting up
setup(
    name="python_datalogger",
    version=VERSION,
    author="Anuja Rahul Gunasinghe",
    author_email="<a.r.gunasinghe@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    keywords=['python', 'logger', 'log_debug', 'log_info', 'log_warning', 'log_error', 'log_critical'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
