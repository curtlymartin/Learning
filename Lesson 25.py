
import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search ('The Adventures of Batman')
mo.group()

