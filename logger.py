import logging
class logger:
    def __init__(self):
            pass
    def logging_message(self,message):
        self.message = message
        logging.basicConfig(filename="linearregression.log",format='%(asctime)s %(message)s',filemode='a')
        logger = logging.getLogger()
        logger.warning(self.message)
        return self.message 


if __name__ == '__main__':
    logs = logger()
    b = logs.logging_message("hello buddy")
    print(b)