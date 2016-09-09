#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.merchant.products.directory_params import DirectoryParams


class GetDirectoryExample(object):

    def example(self):
        with self.__get_client() as client:
            query = DirectoryParams()
            query.currency_code = "EUR"
            query.country_code = "NL"

            response = client.merchant("merchantId").products().directory(809, query)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
