# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class CashPaymentMethodSpecificInputBase(AbstractPaymentMethodSpecificInput):

    def to_dictionary(self):
        dictionary = super(CashPaymentMethodSpecificInputBase, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CashPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        return self
