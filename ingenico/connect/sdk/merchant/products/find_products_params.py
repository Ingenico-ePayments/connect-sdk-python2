# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.param_request import ParamRequest


class FindProductsParams(ParamRequest):
    """
    Query parameters for | Get payment products
    
    See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/find.html
    """

    __country_code = None
    __currency_code = None
    __locale = None
    __amount = None
    __is_recurring = None
    __hide = None

    @property
    def country_code(self):
        """
        | ISO 3166-1 alpha-2 country code
        
        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def currency_code(self):
        """
        | Three-letter ISO currency code representing the currency for the amount
        
        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value):
        self.__currency_code = value

    @property
    def locale(self):
        """
        | Locale used in the GUI towards the consumer. Please make sure that a language pack is configured for the locale you are submitting. If you submit a locale that is not setup on your account we will use the default language pack for your account. You can easily upload additional language packs and set the default language pack in the Configuration Center.
        
        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value):
        self.__locale = value

    @property
    def amount(self):
        """
        | Amount in cents and always having 2 decimals
        
        Type: long
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def is_recurring(self):
        """
        | This allows you to filter payment products based on their support for recurring or not
        
        * true
        * false
        
        | If this is omitted all payment products are returned.
        
        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    @property
    def hide(self):
        """
        | Allows you to hide elements from the response, reducing the amount of data that needs to be returned to your client. Possible options are:
        
        * fields - Don't return any data on fields of the payment product
        * accountsOnFile - Don't return any accounts on file data
        * translations - Don't return any label texts associated with the payment products
        * productsWithoutFields - Don't return products that require any additional data to be captured
        * productsWithoutInstructions - Don't return products that show instructions
        * productsWithRedirects - Don't return products that require a redirect to a 3rd party. Note that products that involve potential redirects related to 3D Secure authentication are not hidden
        
        Type: list[str]
        """
        return self.__hide

    @hide.setter
    def hide(self, value):
        self.__hide = value

    def add_hide(self, value):
        """
        :param value: str
        """
        if self.hide is None:
            self.hide = []
        self.hide.append(value)

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        self._add_parameter(result, "countryCode", self.country_code)
        self._add_parameter(result, "currencyCode", self.currency_code)
        self._add_parameter(result, "locale", self.locale)
        self._add_parameter(result, "amount", self.amount)
        self._add_parameter(result, "isRecurring", self.is_recurring)
        self._add_parameter(result, "hide", self.hide)
        return result
