

class Error(Exception):
    pass

class NullValueError(Error):
    # raised when input is blank
    pass

class NumValueError(Error):
    # raised when input is number when it should be alpha
    pass


class AlphaValueError(Error):
    # raised when input is alpha when it should be number
    pass
