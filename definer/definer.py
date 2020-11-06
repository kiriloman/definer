from definer_client import DefinerClient


class Definer:

    def define(self):
        while True:
            print("""
                    Input a word and 
                    the language the word is in 
                    separated by commas (,).
                    Example: hello,en
                    
                    To exit, type -1.
            """)

            try:
                input_str = input()
            except UnicodeDecodeError:
                print("Only utf-8 characters are supported")
                continue

            if input_str == '-1':
                print("До встречи дружище!")
                break

            data, valid = self.__validate_data(input_str)

            if not valid:
                print(f"The instructions were not followed correctly for {input_str}")
                continue

            word = data[0]
            lang = data[1]

            defined_word = DefinerClient().get_definition(
                word=word.strip(),
                lang=lang.strip(),
            )

            if isinstance(defined_word, dict):
                print(self.__format_definition(defined_word))
            else:
                print(defined_word)

    def __validate_data(self, data: str) -> tuple:
        splitted_data = data.split(',')

        if len(splitted_data) != 2:
            return splitted_data, False

        return splitted_data, True

    def __format_definition(self, data: dict) -> str:
        formatted_definition = ''

        for index, definition_with_examples in enumerate(data['definitions_with_examples']):
            formatted_definition += f"\n{index + 1}. {definition_with_examples['definitions']}"
            formatted_definition += f"\n\t{definition_with_examples['examples']}"

        return f"""
            Definition of {data['word']}:
                {formatted_definition}
        """
