#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.param_request import ParamRequest


class DirectoryParams(ParamRequest):
    """
    Query parameters for Get payment product directory
    See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__products__paymentProductId__directory_get
    
    Attributes:
        currency_code:  str
        country_code:   str
    """

    currency_code = None
    country_code = None

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        self._add_parameter(result, "currencyCode", self.currency_code)
        self._add_parameter(result, "countryCode", self.country_code)
        return result
