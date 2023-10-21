class InputException(Exception):
    """
    Exception raised for errors in invalid input.

    Rules should be like the following sample:
        "{a(x)~>b(x)}"
    Rules should be like the following sample:
        "a": "{<x,0.5>,<y,0.4>}"
    """
    def __init__(self, err):
        """
        :param err: message from error place
        """
        self.message = "Invalid json input. " + err
        super().__init__(self.message)
