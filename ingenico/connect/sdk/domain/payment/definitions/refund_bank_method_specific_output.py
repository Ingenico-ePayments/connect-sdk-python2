# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.domain.payment.definitions.refund_method_specific_output import RefundMethodSpecificOutput


class RefundBankMethodSpecificOutput(RefundMethodSpecificOutput):

    def to_dictionary(self):
        dictionary = super(RefundBankMethodSpecificOutput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundBankMethodSpecificOutput, self).from_dictionary(dictionary)
        return self
