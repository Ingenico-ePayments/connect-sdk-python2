# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.card import Card
from ingenico.connect.sdk.domain.payout.definitions.abstract_payout_method_specific_input import AbstractPayoutMethodSpecificInput


class CardPayoutMethodSpecificInput(AbstractPayoutMethodSpecificInput):

    __card = None
    __payment_product_id = None

    @property
    def card(self):
        """
        | Object containing the card details.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.card.Card`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    @property
    def payment_product_id(self):
        """
        | Payment product identifier
        | Please see payment products <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/paymentproducts.html> for a full overview of possible values.
        
        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    def to_dictionary(self):
        dictionary = super(CardPayoutMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'card', self.card)
        self._add_to_dictionary(dictionary, 'paymentProductId', self.payment_product_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPayoutMethodSpecificInput, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = Card()
            self.card = value.from_dictionary(dictionary['card'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
