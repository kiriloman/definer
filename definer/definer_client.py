import os
import requests
import json


class DefinerClient:

    def __init__(self):
        self.base_url = os.environ.get('DEFINER_EXTERNAL_BASE_URL',
                                       'https://od-api.oxforddictionaries.com/api/v2/entries')
        self.app_id = os.environ.get('DEFINER_APP_ID', 'd09fb097')
        self.app_key = os.environ.get('DEFINER_APP_KEY', '7ad8e0e55a8e50d472addf8820942a2a')

    def get_definition(self, word: str, lang: str):
        url = f"{self.base_url}/{lang.lower()}/{word.lower()}?fields=definitions,examples"

        headers = {
            'app_id': self.app_id,
            'app_key': self.app_key,
        }

        response = requests.get(url, headers=headers)

        response_body = json.loads(response.text)

        if response.status_code != 200:
            return response_body['error']

        return self.__construct_response(response_body)

    def __construct_response(self, data):
        # Constructs a readable response from the external
        # API documented at https://developer.oxforddictionaries.com/documentation/making-requests-to-the-api

        response = {
            'word': data['word'],
        }

        definitions_with_examples = []

        results = data['results']

        for result in results:
            for lexical_entry in result['lexicalEntries']:
                for entry in lexical_entry['entries']:
                    for sense in entry['senses']:
                        definitions_with_examples.append(
                            {
                                'definitions': '\n'.join(sense['definitions']),
                                'examples': '\n\t'.join([ex['text'] for ex in sense.get('examples', [])]),
                            }
                        )

        response['definitions_with_examples'] = definitions_with_examples

        return response
