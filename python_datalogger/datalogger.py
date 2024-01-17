"""
simplifies the python data logging process for quicker and easier data logging.

Author: Anuja Rahul
python_datalogger/datalogger.py
"""
import os
import time
import logging
import datetime as dt
from typing import Callable


class DataLogger:
    """
    Records and log any type of requests specified by the user
    levels = (debug, info, warning, error, critical)

    Attributes:
    ----------

        log_path (string): Path to the log file
        levels (list): List of logger security levels

    Methods:
    -------

        Private:

            __init_env : initiates the required directories for saving log files
            __set_logger : sets the logger security levels prior to logging

        Public:

            logger : decorator to log basic exceptions
            log_debug : logs the debug logs
            log_info : logs the info logs
            log_warning : logs the warning logs
            log_error: logs the error logs
            log_critical : logs the critical logs


    """

    log_path = f"{os.getcwd()}/logs"
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    def __init__(self, name: str = "DataLogger", propagate: bool = False, level: str = "DEBUG"):
        """
        Creates a new instance of the DataLogger class
        :param name: name of the logger
        :param propagate: True/False, If true the logger display the logs on console
        :param level: security level of the logger
        """

        DataLogger.__init_env()
        DataLogger.__set_logger(DataLogger.levels[level.upper()])
        self.__today = dt.datetime.today()
        self.__filename = (f"{DataLogger.log_path}/{self.__today.day:02d}-{self.__today.month:02d}-"
                           f"{self.__today.year}.log")
        self.__logger = logging.getLogger(name)
        self.__logger.propagate = propagate   # Enables/Disables logger from displaying in console
        self.__file_handler = logging.FileHandler(self.__filename)
        self.__formatter = logging.Formatter("%(asctime)s: %(name)s - %(levelname)s - %(message)s")
        self.__file_handler.setFormatter(self.__formatter)
        self.__logger.addHandler(self.__file_handler)

    @classmethod
    def __init_env(cls):
        """Initiates the required directories for the log files"""
        try:
            os.mkdir(DataLogger.log_path)
        except FileExistsError:
            pass

    @staticmethod
    def __set_logger(level) -> None:
        """
        Set the logging security level.
        :param level: level of the logging (default:DEBUG)
        """
        for handler in logging.root.handlers:
            logging.root.removeHandler(handler)
        logging.basicConfig(level=level)

    @staticmethod
    def logger(function: Callable) -> Callable:
        """Decorator to time functions and log any errors of a function"""
        method_name = function.__name__
        error_logger = DataLogger(name="ErrorLogger", level="ERROR", propagate=True)
        info_logger = DataLogger(name="InfoLogger", level="INFO", propagate=False)

        def wrapper(*args, **kwargs):
            try:
                before = time.time()
                result = function(*args, **kwargs)
                after = time.time()
                info_logger.log_info(f"[{method_name}] - executed successfully in {(after - before):.10f} seconds.")
                return result
            except Exception as exception:
                error_logger.log_error(f"[{method_name}] - {exception}")

        return wrapper

    def log_debug(self, info: str) -> None:
        """log a debug log."""
        self.__logger.debug(info)

    def log_info(self, info: str) -> None:
        """log an info log."""
        self.__logger.info(info)

    def log_warning(self, info: str) -> None:
        """log a warning log."""
        self.__logger.warning(info)

    def log_error(self, info: str) -> None:
        """log an error log."""
        self.__logger.error(info)

    def log_critical(self, info: str) -> None:
        """log a critical log."""
        self.__logger.critical(info)

    def __repr__(self):
        return f"[logger={self.__logger.name}, propagate={self.__logger.propagate}, path={self.__filename}]"
