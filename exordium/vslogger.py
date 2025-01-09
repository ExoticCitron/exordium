import sys
import datetime
import inspect
import os

class VSCodeLogger:
    COLORS = {
        'INFO': '\033[92m',     # Green
        'DEBUG': '\033[96m',    # Cyan
        'WARNING': '\033[93m',  # Yellow
        'SUCCESS': '\033[94m',  # Blue
        'ERROR': '\033[91m',    # Red
        'CRITICAL': '\033[95m', # Magenta
        'RESET': '\033[0m'      # Reset color
    }

    def __init__(self, name):
        self.name = name

    def _log(self, level, message):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        caller = inspect.currentframe().f_back.f_back
        filename = os.path.basename(caller.f_code.co_filename)
        lineno = caller.f_lineno
        func_name = caller.f_code.co_name

        log_message = (
            f"{current_time} ~ "
            f"{self.COLORS[level]}{level}{self.COLORS['RESET']} | "
            f"{self.name}:{func_name}:{lineno} - "
            f"{self.COLORS[level]}{message}{self.COLORS['RESET']}"
        )
        print(log_message, file=sys.stderr)

    def info(self, message):
        self._log('INFO', message)

    def debug(self, message):
        self._log('DEBUG', message)

    def warning(self, message):
        self._log('WARNING', message)

    def success(self, message):
        self._log('SUCCESS', message)

    def error(self, message):
        self._log('ERROR', message)

    def critical(self, message):
        self._log('CRITICAL', message)

def get_logger(name):
    return VSCodeLogger(name)