from mimesis import Person
from mimesis.enums import Gender

from collections import OrderedDict

from pprint import pprint

def get_card(gender):
    person = Person('uk')
    return OrderedDict(id=person.identifier(mask='##-##/##'),
                       full_name=person.full_name(gender),
                       age=person.age(minimum=18, maximum=66),
                       occupation=person.occupation(),
                       telephone=person.telephone(mask='', placeholder='#'),
                       email=person.email(domains=('@yandex.ru', '@gmail.com')),
                       username=person.username(template='UU_d'),
                       password=person.password(length=8, hashed=True))

pprint(get_card(Gender.MALE))

