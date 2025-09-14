import logging
from .utils import calc

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class RPNCalculator:
    def __init__(self) -> None:
        self.stack = []

    def run(self) -> None:
        while True:
            inp = input("> ")
            if inp == "q":
                return
            elif inp == "p":
                print(self.stack)
            else:
                self.evaluate(inp)

    def err(self, msg: str) -> None:
        logger.error(msg)

    def evaluate(self, inp: str) -> None:
        try:
            self.stack.append(float(inp))
            return
        except ValueError:
            pass

        if inp not in ["+", "-", "*", "/"]:
            self.err(
                f"Invalid input: {inp}")
            raise ValueError(f"Invalid input: {inp}")

        # TODO: Handle the case where there are not enough operands in the stack (Bonus Point)

        b = self.stack.pop()
        a = self.stack.pop()

        try:
            res = calc(a, b, inp)
        except ZeroDivisionError:
            self.err("Division by zero")
            raise ZeroDivisionError("Division by zero")

        self.stack.append(res)
        print(res)


if __name__ == "__main__":
    rpn = RPNCalculator()
    rpn.run()
