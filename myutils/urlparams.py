'''
# URLParams Module

    Decodes params in a URL then returns them as a `dict`
'''
def GetParams(url) -> dict:
    # Decodes the url component
    params = {item.split('=')[0]: item.split('=')[1]
              for item in url.split('?')[1].split('&')}    
    return params