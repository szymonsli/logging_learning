import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/calculator_log.log",
    filemode="a",
    format="""%(asctime)s - %(levelname)s - %(module)s::%(funcName)s - %(message)s""",
    datefmt="%d-%m-%Y %H:%M:%S"
)


class Calculator:
    def __init__(self, first_number):
        self.current_number = first_number
        logging.info(f"The current number is {self.current_number}")

    def add(self, number):
        self.current_number += number
        logging.debug(f"The current number is {self.current_number}")

    def subtract(self, number):
        self.current_number -= number
        logging.warning(f"The current number is {self.current_number}")

    def multiply(self, number):
        self.current_number *= number
        logging.error(f"The current number is {self.current_number}")

    def divide(self, number):
        self.current_number /= number
        logging.critical(f"The current number is {self.current_number}")


c1 = Calculator(4)
c1.add(2)
c1.divide(3)
c1.subtract(2)
c1.multiply(5)
