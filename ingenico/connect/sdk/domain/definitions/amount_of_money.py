# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class AmountOfMoney(DataObject):

    __amount = None
    __currency_code = None

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
    def currency_code(self):
        """
        | Three-letter ISO currency code representing the currency for the amount
        
        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value):
        self.__currency_code = value

    def to_dictionary(self):
        dictionary = super(AmountOfMoney, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amount', self.amount)
        self._add_to_dictionary(dictionary, 'currencyCode', self.currency_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AmountOfMoney, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        if 'currencyCode' in dictionary:
            self.currency_code = dictionary['currencyCode']
        return self
