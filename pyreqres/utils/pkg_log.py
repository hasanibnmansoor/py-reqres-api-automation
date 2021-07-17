import logging
import sys

__all__ = ["logger"]


FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s"
)


def console_log():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def log(logger_name, log_level=logging.INFO):
    log_handler = logging.getLogger(logger_name)
    log_handler.setLevel(log_level)
    log_handler.addHandler(console_log())
    log_handler.propagate = False
    return log_handler


logger = log("pyreqres")
