from logger import logger


class Calculator:
    def __init__(self, first_number):
        self.input_number = first_number
        self.result = self.input_number
        logger.info(f"The current number is {self.result}")

    def add(self, number):
        self.result += number
        logger.debug(f"Added {number}. The result is {self.result}")

    def subtract(self, number):
        self.result -= number
        logger.debug(f"Subtracted {number}. The result is {self.result}")

    def multiply(self, number):
        self.result *= number
        logger.debug(f"Multiplied by {number}. The result is {self.result}")

    def divide(self, number):
        try:
            self.result /= number
        except ZeroDivisionError:
            logger.error("Tried to divide by 0. Skipped operation.")
        else:
            logger.debug(f"Divided by {number}. The result is {self.result}")


c1 = Calculator(4)
c1.add(2)
c1.divide(3)
c1.subtract(1)
c1.multiply(5)
c1.divide(2)
c1.divide(0)
c1.add(13)
