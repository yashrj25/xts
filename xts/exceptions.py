# exception and responses

import json
import requests
from requests import exceptions
from requests.exceptions import HTTPError
from requests import ConnectTimeout, HTTPError, Timeout, ConnectionError


class XTSException(Exception):
    """
    Base exception class representing a XTS client exception.

    Every specific XTS client exception is a subclass of this
    and  exposes two instance variables `.code` (HTTP error code)
    and `.message` (error text).
    """

    def __init__(self, message, code=500):
        # initialize the exception
        super(XTSException, self).__init__(message)
        self.code = code


class XTSGeneralException(XTSException):
    # an unclassified, general error
    # default code is 500

    def __init__(self, message, code=500):
        # initialize the exception
        super(XTSGeneralException, self).__init__(message, code)


class XTSTokenException(XTSException):
    # represents all token and authentication related errors
    # default code is 400

    def __init__(self, message, code=400):
        # initialize the exception
        super(XTSTokenException, self).__init__(message, code)


class XTSPermissionException(XTSException):
    # represents permission denied exceptions for certain calls
    # default code is 400

    def __init__(self, message, code=400):
        # initialize the exception
        super(XTSPermissionException, self).__init__(message, code)


class XTSOrderException(XTSException):
    # represents all order placement and manipulation errors
    # default code is 500

    def __init__(self, message, code=400):
        # initialize the exception
        super(XTSOrderException, self).__init__(message, code)


class XTSInputException(XTSException):
    # represents user input errors such as missing and invalid parameters
    # default code is 400

    def __init__(self, message, code=400):
        # initialize the exception
        super(XTSInputException, self).__init__(message, code)


class XTSDataException(XTSException):

    # represents a bad response from the backend Order Management System (OMS)
    # default code is 500.

    def __init__(self, message, code=500):
        # initialize the exception
        super(XTSDataException, self).__init__(message, code)


class XTSNetworkException(XTSException):

    # represents a network issue between XTS and the backend Order Management System (OMS)
    # default code is 500

    def __init__(self, message, code=500):
        # initialize the exception
        super(XTSNetworkException, self).__init__(message, code)
