# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.additional_order_input_airline_data import AdditionalOrderInputAirlineData
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.riskassessments.definitions.customer_risk_assessment import CustomerRiskAssessment


class OrderRiskAssessment(DataObject):

    __additional_input = None
    __amount_of_money = None
    __customer = None

    @property
    def additional_input(self):
        """
        | Object containing additional input on the order
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.additional_order_input_airline_data.AdditionalOrderInputAirlineData`
        """
        return self.__additional_input

    @additional_input.setter
    def additional_input(self, value):
        self.__additional_input = value

    @property
    def amount_of_money(self):
        """
        | Object containing amount and ISO currency code attributes
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value):
        self.__amount_of_money = value

    @property
    def customer(self):
        """
        | Object containing the details of the consumer
        
        Type: :class:`ingenico.connect.sdk.domain.riskassessments.definitions.customer_risk_assessment.CustomerRiskAssessment`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    def to_dictionary(self):
        dictionary = super(OrderRiskAssessment, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalInput', self.additional_input)
        self._add_to_dictionary(dictionary, 'amountOfMoney', self.amount_of_money)
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderRiskAssessment, self).from_dictionary(dictionary)
        if 'additionalInput' in dictionary:
            if not isinstance(dictionary['additionalInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['additionalInput']))
            value = AdditionalOrderInputAirlineData()
            self.additional_input = value.from_dictionary(dictionary['additionalInput'])
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerRiskAssessment()
            self.customer = value.from_dictionary(dictionary['customer'])
        return self
