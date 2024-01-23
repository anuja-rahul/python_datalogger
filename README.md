## python_datalogger (v0.0.2)
#### Simplified datalogger using python for easier and faster data logging.

    Datalogger will record all the recorded logs in a local directory (./logs)

## How to install datalogger from test-pypi
    
#### Run on your terminal :
    pip install -i https://test.pypi.org/simple/ python-datalogger


## How to install datalogger locally

    01. Download this project.
    02. Extract the master zip file
    03. Open command prompt in the master folder location
    04. Run (for windows) -> pip install . 
        Run (for mac)     -> pip3 install .

    Now you can use datalogger locally any time you want


### How to use Datalogger.logger decorator for basic exception handling. (Example):
```python

from python_datalogger import DataLogger


# using datalogger decorator to record basic exceptions
@DataLogger.logger
def test_method(num: int) -> float:
    return 1000/num


test_method(2)  # if no exceptions are encountered, logs the time taken for this method to run

# raises ZeroDivisionError for demonstration
test_method(0) # logs the error, in case of an exception

```

### How to use Datalogger.timeit decorator to time a function runtime.
```python
from python_datalogger import DataLogger

@DataLogger.timeit
def test_method(num: int) -> float:
    return 1000/num

test_method(10) # displays the runtime before returning the result for test_method
```

### How to use datalogger for specific info logging. (Example):
```python

from python_datalogger import DataLogger
    

logger = DataLogger(name="TestLogger", level="DEBUG", propagate=True)

# name can be any name you like for the current instance of the Datalogger
# level has 5 security options (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# propagate has 2 options (True/False), if true, the current log is displayed on the terminal


def test_method():
    try:
        print("Starting to do something !")

        # logs a regular information log
        logger.log_info("test_method did something !")

    except Exception as exception:

        # in case of an exception, logs an error log containing the specified exception
        logger.log_error(str(exception))

test_method()

```


### There are 5 possible types of logging methods you can use for each security level.

```python
from python_datalogger import DataLogger

logger = DataLogger(name="TestLogger", level="DEBUG", propagate=True)
    
logger.log_debug(info="this is a debug log")
logger.log_info(info="this is an info log")
logger.log_warning(info="this is a warning log")
logger.log_error(info="this is an error log")
logger.log_critical(info="this is a critical log")

"""Each of these methods accept one (string) parameter containing the information you want to log."""

```
    
    
    