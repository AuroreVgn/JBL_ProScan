"""Exceptions for JBL ProScan."""


class JBLProScanError(Exception):
    """Base JBL ProScan exception."""


class JBLProScanAuthenticationError(JBLProScanError):
    """Authentication failed."""


class JBLProScanConnectionError(JBLProScanError):
    """Connection failed."""


class JBLProScanParseError(JBLProScanError):
    """JBL page could not be parsed."""
