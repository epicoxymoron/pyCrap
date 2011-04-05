from datetime import datetime
from sys import stderr

class Logger(object):
    """A logging facility somewhat like Log4J"""

    class LogLevel(object):
        """A log level to be used as an enumeration"""
        def __init__(self, str_level, int_level):
            self.str_level = str_level
            self.int_level = int_level
        def __eq__(self, other):
            return self.int_level == other.int_level
        def __ne__(self, other):
            return not self.__eq__(other)
        def __lt__(self, other):
            return self.int_level < other.int_level
        def __gt__(self, other):
            return not self.__lt__(other)
        def __le__(self, other):
            return self.__lt__(other) or self.__eq__(other)
        def __ge__(self, other):
            return self.__gt__(other) or self.__eq__(other)
        def __str__(self):
            return self.str_level

    DEBUG = LogLevel("DEBUG", 1 << 0)
    INFO = LogLevel("INFO", 1 << 1)
    WARN = LogLevel("WARN", 1 << 2)
    ERROR = LogLevel("ERROR", 1 << 3)
    CRITICAL = LogLevel("CRITICAL", 1 << 4)
    FATAL = LogLevel("FATAL", 1 << 5)

    def __init__(self, log_level=WARN, log_event_interval=250, 
            destination=stderr):
        self.log_event_interval = log_event_interval
        self.log_level = log_level
        self.destination = destination
        self.last_flush = None
        self.events = []

    def _log(self, level, event):
        """Logs an event with the specified logging level"""
        if level >= self.log_level:
            self.destination.write("{0}\t{1}\t{2}\n".format(
                str(datetime.utcnow()), level, event))
        
    def debug(self, event):
        """Writes a debug-level log message.  
        Use this to learn about the goings-on of your program"""
        self._log(Logger.DEBUG, event)

    def info(self, event):
        """Writes a info-level log message.  
        Use this for general information"""
        self._log(Logger.INFO, event)

    def warn(self, event):
        """Writes a info-level log message.  
        Use this when something may be compromised"""
        self._log(Logger.WARN, event)

    def error(self, event):
        """Writes a error-level log message.  
        Use this for recoverable errors"""
        self._log(Logger.ERROR, event)

    def critical(self, event):
        """Writes a critical-level log message.  
        Use this for recoverable, but major errors"""
        self._log(Logger.CRITICAL, event)

    def fatal(self, event):
        """Writes a fatal-level log message.  
        Use this for unrecoverable errors"""
        self._log(Logger.FATAL, event)

