import inspect
import logging
import os.path as path
import os

def customLogger(logLevel=logging.DEBUG):
    # Get the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logLevel)
    if not logger.handlers:
        log_filename = 'automation.log'

        log_folder = path.normpath(path.join(path.dirname(path.abspath(__file__)), '..', 'log'))
        try:
            os.makedirs(log_folder)
        except FileExistsError:
            pass

        log_full_path = path.normpath(path.join(log_folder, log_filename))

        fileHandler = logging.FileHandler(log_full_path, mode='a')
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter("%(asctime)s.%(msecs)03d [%(levelname)-8s] [%(name)s]: %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

    return logger