# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class DecryptedPaymentData(DataObject):

    __cardholder_name = None
    __cryptogram = None
    __dpan = None
    __eci = None
    __expiry_date = None

    @property
    def cardholder_name(self):
        """
        | Card holder's name on the card. This maps to the following field in the vendor's encrypted payment data:
        
        * Apple Pay: PKPayment.token.paymentData.data.cardholderName
        * Android Pay: Not Available
        
        Type: str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value):
        self.__cardholder_name = value

    @property
    def cryptogram(self):
        """
        | The 3D secure online payment cryptogram. This maps to the following field in the vendor's encrypted payment data:
        
        * Apple Pay: PKPayment.token.paymentData.data.paymentData.onlinePaymentCryptogram
        * Android Pay: FullWallet.paymentMethodToken.token.encryptedMessage.3dsCryptogram
        
        Type: str
        """
        return self.__cryptogram

    @cryptogram.setter
    def cryptogram(self, value):
        self.__cryptogram = value

    @property
    def dpan(self):
        """
        | The device specific PAN. This maps to the following field in the vendor's encrypted payment data:
        
        * Apple Pay: PKPayment.token.paymentData.data.applicationPrimaryAccountNumber
        * Android Pay: FullWallet.paymentMethodToken.token.encryptedMessage.dpan
        
        Type: str
        """
        return self.__dpan

    @dpan.setter
    def dpan(self, value):
        self.__dpan = value

    @property
    def eci(self):
        """
        | Electronic Commerce Indicator. This maps to the following field in the vendor's encrypted payment data:
        
        * Apple Pay: PKPayment.token.paymentData.data.paymentData.eciIndicator
        * Android Pay: FullWallet.paymentMethodToken.token.encryptedMessage.3dsEciIndicator
        
        Type: int
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value

    @property
    def expiry_date(self):
        """
        | Expiry date of the card
        | Format: MMYY. This maps to the following field in the vendor's encrypted payment data:
        
        * Apple Pay: PKPayment.token.paymentData.data.applicationExpirationDate
        * Android Pay:FullWallet.paymentMethodToken.token.encryptedMessage.expirationMonth and FullWallet.paymentMethodToken.token.encryptedMessage.expirationYear
        
        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self.__expiry_date = value

    def to_dictionary(self):
        dictionary = super(DecryptedPaymentData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cardholderName', self.cardholder_name)
        self._add_to_dictionary(dictionary, 'cryptogram', self.cryptogram)
        self._add_to_dictionary(dictionary, 'dpan', self.dpan)
        self._add_to_dictionary(dictionary, 'eci', self.eci)
        self._add_to_dictionary(dictionary, 'expiryDate', self.expiry_date)
        return dictionary

    def from_dictionary(self, dictionary):
        super(DecryptedPaymentData, self).from_dictionary(dictionary)
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'cryptogram' in dictionary:
            self.cryptogram = dictionary['cryptogram']
        if 'dpan' in dictionary:
            self.dpan = dictionary['dpan']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
