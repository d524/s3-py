from logging import getLogger, StreamHandler, DEBUG


class Log:
    def __init__(self):
        self.logger = getLogger(__name__)

    def getLogger(self):
        return self.logger

    def configure(self):
        self.setHandler()
        self.setLogLevel()
        logger.propagate = False

    def setHandler(self):
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        self.logger.addHandler(handler)

    def setLogLevel(parameter_list):
        self.logger.setLevel(DEBUG)
