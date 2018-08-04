import hmac
import json
import hashlib
import inspect
import requests
import collections

from typing import Dict
from typing import List


class ApiBase:
    """ The Base Class for all api files."""

    def __init__(self, connectionstring: str, privatekey: str):

        self.baseUrl = connectionstring
        self.privateKey = privatekey

    @staticmethod
    def generate_signature(parameters: Dict[str, str], privatekey: str):
        """ Generates a Haas Signature to be appended at the end of the url request

        :param parameters: Dict[str,str]: The parameter list to encode 
        :param privatekey: str: The haas secret key to use for the signature

        :returns: Tuple(str,str): A tuple with the parameter string and the signature
        """

        parameter_string = ""

        parameters = collections.OrderedDict(sorted(parameters.items()))

        for key, value in parameters.items():
            parameter_string += "&" + str(key) + "=" + str(value)

        parameter_string = parameter_string.replace("&", "", 1)

        key = bytes(privatekey, 'UTF-8')
        message = bytes(parameter_string, 'UTF-8')

        digester = hmac.new(key, message, hashlib.sha256)
        signature = digester.digest()
        signature = signature.hex().replace("-", "").upper()

        return parameter_string, signature

    def _execute_request(self, endpoint: str, parameters: Dict[str, str]):
        """ Sends a get request to the specified endpoint with parameters set.

        :param endpoint: str: URL endpoint for action to be placed Ex. /GetOpenOrders
        :param parameters: Dict[str,str]: Parameter list to send to the endpoint

        :returns: JsonObject: Returns a json object of the response.
        """

        url = self.baseUrl + endpoint

        # Authorize is set by default
        parameters = collections.OrderedDict(sorted(parameters.items()))

        paramSig = ApiBase.generate_signature(parameters, self.privateKey)

        if not paramSig[0]:
            url = url + "?sig="+paramSig[1]
        else:
            url = url + "?"
            url = url + paramSig[0]
            url = url + "&sig="+paramSig[1]

        #print(url)
        #return requests.get(url).json()
        #test = requests.get(url).json()
        #print(test)
        try:
            return requests.get(url).json()
        except:
            context = {"ErrorCode": 9002,
                       "ErrorMessage": "Failed To Connect To The Haasonline Trade Server",
                       "Result": {}}
            return json.loads(json.dumps(context))

    @staticmethod
    def _from_json(data, cls):
        """ Converts a json response to a class object. Can only go 2 nested deep

        :param data: Json data object 
        :parama cls: Class type to convert to

        :returns: any: A instance of the specified class
        """

        if type(data) is dict:
            annotations: dict = cls.__annotations__ if hasattr(cls, '__annotations__') else None
            if issubclass(cls, List):
                list_type = cls.__args__[0]
                instance: list = list()
                for value in data:
                    instance.append(ApiBase._from_json(value, list_type))
                return instance
            elif issubclass(cls, Dict):
                    key_type = cls.__args__[0]
                    val_type = cls.__args__[1]
                    instance: dict = dict()
                    for key, value in data.items():
                        instance.update({ApiBase._from_json(key, key_type): ApiBase._from_json(value, val_type)})
                    return instance
            else:
                instance: cls = cls()

                for name, value in data.items():

                    if name == "GUID":
                        name = "guid"
                    elif name == "ROI":
                        name = "roi"
                    else:
                        func = lambda s: s[:1].lower() + s[1:] if s else ''
                        name = func(name)
                        field_type = annotations.get(name)

                    if inspect.isclass(field_type) and isinstance(value, (dict, tuple, list, set, frozenset)):
                        setattr(instance, name, ApiBase._from_json(value, field_type))
                    else:
                        setattr(instance, name, value)
                return instance
        return data



