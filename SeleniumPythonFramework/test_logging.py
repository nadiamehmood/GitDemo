import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logFile.log')   # where to print logs
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # how to print logs
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    # what to print in logs
    # if we want to print only errors logs then we need to define levels in logs
    # if i set level to error then error and critical logs will be printed
    # if i set level to warning then warning, error and critical logs will be printed
    logger.setLevel(logging.INFO)                  # it will print logs from level info(level 2) to critical(level 5)
    logger.debug("A debug statement is executed")  # level 1
    logger.info("Information statement")           # level 2
    logger.debug("A debug statement is executed")  # even if i write debug below info it will not print bcz order matters
    logger.warning("Something is in warning mode") # level 3
    logger.error("A major error happened")         # level 4
    logger.critical("Critical issue")              # level 5

