# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RetailDecisionsCCFraudCheckOutput(DataObject):

    __fraud_code = None
    __fraud_neural = None
    __fraud_rcf = None

    @property
    def fraud_code(self):
        """
        | Provides additional information about the fraud result
        
        Type: str
        """
        return self.__fraud_code

    @fraud_code.setter
    def fraud_code(self, value):
        self.__fraud_code = value

    @property
    def fraud_neural(self):
        """
        | The raw score returned by the Neural check returned by the evaluation of the transaction
        
        Type: str
        """
        return self.__fraud_neural

    @fraud_neural.setter
    def fraud_neural(self, value):
        self.__fraud_neural = value

    @property
    def fraud_rcf(self):
        """
        | List of RuleCategoryFlags as setup in the Retail Decisions system that lead to the result
        
        Type: str
        """
        return self.__fraud_rcf

    @fraud_rcf.setter
    def fraud_rcf(self, value):
        self.__fraud_rcf = value

    def to_dictionary(self):
        dictionary = super(RetailDecisionsCCFraudCheckOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'fraudCode', self.fraud_code)
        self._add_to_dictionary(dictionary, 'fraudNeural', self.fraud_neural)
        self._add_to_dictionary(dictionary, 'fraudRCF', self.fraud_rcf)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RetailDecisionsCCFraudCheckOutput, self).from_dictionary(dictionary)
        if 'fraudCode' in dictionary:
            self.fraud_code = dictionary['fraudCode']
        if 'fraudNeural' in dictionary:
            self.fraud_neural = dictionary['fraudNeural']
        if 'fraudRCF' in dictionary:
            self.fraud_rcf = dictionary['fraudRCF']
        return self
