'''
# UserIO module

    provides some handy functions for command line interfacing
'''
import unicodedata,logging
cancel = 'q'
logger = logging.getLogger('UserIO')
class UserCannceledException(Exception):
    def __init__(self, *args, **kwargs):
        logger.warn('Intercepted user canncel action')
        super().__init__(*args, **kwargs)

def get(*args,**kwargs):
    '''Input but wrapped with print() and added interruptions
    
        Set `ignore_cancel=True` if you don't want keyboard interruptions
    ''' 
    ignore_cancel = kwargs['ignore_cancel'] if 'ignore_cancel' in kwargs.keys() else False

    kwargs = {k:v for k,v in kwargs.items() if not k in ['ignore_cancel']}
    # Reverved keyword agrument
    print(*args,**{'end':'>>>',**kwargs})
    try:
        result = input()
    except KeyboardInterrupt:
        result = cancel
    
    if result == cancel and not ignore_cancel:raise UserCannceledException('Cannceled.')
    return result

def scrlen(s):
    return sum([2 if unicodedata.east_asian_width(i) in 'WFA' else 1 for i in s])

def listout(items,foreach=lambda x,i: x,title='LIST',showindex=True,reverse=False):
    '''Prints a list of dictionaries with their index and value processed by `foreach`'''
    print(title,'_' * (50 - scrlen(title)),sep='')
    items = list(items)
    if items:
        for index in reversed(range(0,len(items))) if reverse else range(0,len(items)):
            item = items[index]
            try:
                print(*('',str(index).ljust(5)) if showindex else '',foreach(item,index),sep=' ' if showindex else '')
            except Exception as e:
                print(*('',str(index).ljust(5)) if showindex else '','-',sep=' ' if showindex else '')
    else:
        print('X     无可用操作')
    print('_' * 50)