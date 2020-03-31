'''
# Js2Dict Module

    Turns js varaibles into dictionaries
'''
import re,json
regex = r"(?:var|^|)([ a-zA-Z0-9]*)(?:=)([^;$)]*)(?:;|$)"

def js2dict(js):
    result = {}
    for matches in re.finditer(regex,js):
        key,value = matches.groups()
        key,value=key.strip(),value.strip()
        value = value[:-1] if value[-1:] == ';' else value
        if key in result.keys():result[key].append(value)
        else:result[key] = [value]
    return result