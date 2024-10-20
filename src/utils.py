from src.logger import logging
import sys
from src.exception import CustomException


if __name__ == "__main__":
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        logging.error("Division by zero error occurred", exc_info=True)
        raise CustomException(e, sys)
