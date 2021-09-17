import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]    # it gives you the name of method from which the method will call
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logFile.log')  # where to print logs
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # how to print logs
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger


