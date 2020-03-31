'''
# Cookie2Dict Module

    Turns cookie strings into a dictionary
'''
def cookie2dict(src):
    args = {b.split('=')[0].strip():b.split('=')[1].strip() for b in src.split(';')}
    return args
