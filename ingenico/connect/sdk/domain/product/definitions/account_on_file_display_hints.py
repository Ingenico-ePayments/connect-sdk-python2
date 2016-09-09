#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.label_template_element import LabelTemplateElement


class AccountOnFileDisplayHints(DataObject):
    """
    Class AccountOnFileDisplayHints
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AccountOnFileDisplayHints
    
    Attributes:
        label_template:  list[:class:`LabelTemplateElement`]
        logo:            str
     """

    label_template = None
    logo = None

    def to_dictionary(self):
        dictionary = super(AccountOnFileDisplayHints, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'labelTemplate', self.label_template)
        self._add_to_dictionary(dictionary, 'logo', self.logo)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AccountOnFileDisplayHints, self).from_dictionary(dictionary)
        if 'labelTemplate' in dictionary:
            if not isinstance(dictionary['labelTemplate'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['labelTemplate']))
            self.label_template = []
            for labelTemplate_element in dictionary['labelTemplate']:
                labelTemplate_value = LabelTemplateElement()
                self.label_template.append(labelTemplate_value.from_dictionary(labelTemplate_element))
        if 'logo' in dictionary:
            self.logo = dictionary['logo']
        return self
