import logging
logging.basicConfig(level=logging.INFO)


def loggingDecorator(func):
    def wrapperLogging(*args, **kwargs):
        logging.info(f"Start Func={func.__name__}")
        func(*args, **kwargs)
        logging.info(f"Finished Func={func.__name__}")
    return wrapperLogging


@loggingDecorator
def showInfo(*args, **kwargs):
    print(f"This is test function, args={args}, kwargs={kwargs}")


if __name__ == "__main__":
    showInfo('arg1', 'arg2', kwarg1=1, kwarg2=2)
