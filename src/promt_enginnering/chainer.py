class Chainer:
    """
    A simple class to chain together multiple functions or callables.
    Each function's output is passed as input to the next function.
    """

    def __init__(self, *functions):
        self.functions = functions

    def __call__(self, input_data):
        result = input_data
        for func in self.functions:
            result = func(result)
        return result

    def add(self, func):
        """Add a new function to the chain."""
        self.functions += (func,)


# Example usage:
if __name__ == "__main__":
    def step1(x):
        return x + 1

    def step2(x):
        return x * 2

    chainer = Chainer(step1, step2)
    output = chainer(3)  # (3 + 1) * 2 = 8
    print(output)