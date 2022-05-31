from abc import ABCMeta, abstractmethod


class ObfuscationCapable(object):
    """
    Classes that extend this class support obfuscating bodies and headers.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def set_body_obfuscator(self, body_obfuscator):
        """
        Sets the current body obfuscator to use.
        """
        raise NotImplementedError

    @abstractmethod
    def set_header_obfuscator(self, header_obfuscator):
        """
        Sets the current header obfuscator to use.
        """
        raise NotImplementedError
