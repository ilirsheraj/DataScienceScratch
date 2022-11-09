class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    def __init__(self, count=0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times=1):
        """Click the clicker some number of times."""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


clicker = CountingClicker()
print(clicker.count)
clicker.click()
clicker.click()
print(clicker.count)
clicker.reset()
print(clicker.count)


# A subclass inherits all the behavior of its parent class.
class NoResetClicker(CountingClicker):
    # This class has all the same methods as CountingClicker

    # Except that it has a reset method that does nothing.
    def reset(self):
        pass


clicker2 = NoResetClicker()
print(clicker2.count)
clicker2.click()
print(clicker2.count)
clicker2.reset()
print(clicker2.count)
