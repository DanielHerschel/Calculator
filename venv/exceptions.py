class ComplexNumberError(Exception):
    """
    Exception is raised when gotten a complex number.
    """

    def __init__(self, message="Can't use complex numbers."):
        """
        Constructor.
        """
        self.message = message
        super().__init__(self.message)


class InfiniteNumberError(Exception):
    """
    Exception is raised when gotten an infinite number.
    """

    def __init__(self, message="Can't use infinite numbers."):
        """
        Constructor.
        """
        self.message = message
        super().__init__(self.message)


class NegativeFactorialError(Exception):
    """
    Exception is raised when trying to factorialize a negative number.
    """

    def __init__(self, message="Can't factorialize numbers below 0."):
        """
        Constructor.
        """
        self.message = message
        super().__init__(self.message)


class DecimalFactorialError(Exception):
    """
    Exception is raised when trying to factorialize a decimal number.
    """

    def __init__(self, message="Can't factorialize decimal numbers."):
        """
        Constructor.
        """
        self.message = message
        super().__init__(self.message)
