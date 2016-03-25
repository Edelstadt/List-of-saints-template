
import sys
from glob import glob

from lxml import etree
from colorama import init as colorama_init, Fore


SCHEMA_FILENAME = 'saints.xsd'


def validate():
    colorama_init()

    try:
        print(Fore.YELLOW + "Reading schema '{}'.".format(SCHEMA_FILENAME))
        with open(SCHEMA_FILENAME, 'rb') as f:
            file_contents = f.read()

        schema = etree.XMLSchema(etree.XML(file_contents))
        parser = etree.XMLParser(schema=schema)

        for filename in glob('*.xml'):
            print(Fore.YELLOW + "Validating '{}'.".format(filename))
            with open(filename, 'rb') as f:
                file_contents = f.read()
            etree.fromstring(file_contents, parser)

    except Exception as e:
        print(Fore.RED + 'Something is not valid!\n\n' + Fore.RESET)
        print(e)
    else:
        print(Fore.GREEN + 'Everything is OK!')


if __name__ == '__main__':
    validate()
