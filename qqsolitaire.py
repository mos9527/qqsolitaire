import requests
import json
import re
import time
import sys
import logging
import coloredlogs

from myutils import userio, js2dict, cookie2dict
coloredlogs.install(logging.DEBUG)

if len(sys.argv)<2:
    print('使用：python qqunsolitaire.py [加群分享文本] [cookie]')
    sys.exit()

_,share_url,cookies = sys.argv


def _bkn(skey):
    '''bkn:for csrf token'''
    mask1, mask2 = 5381, 0x7FFFFFFF
    # ‭1 0101 0000 0101‬ and ‭111 1111 1111 1111 1111 1111 1111 1111‬
    for char in skey:
        mask1 = mask1 + ((mask1 << 5) + ord(char))
    return mask1 & mask2


cookies = cookie2dict.cookie2dict(cookies)
s = requests.Session()
s.cookies.update(cookies)


def getRawUin(share_url):
    '''Fetches real ID of `QQqun`'''
    regex = '(?<=rawuin = )\d*'
    r = s.get(share_url).text
    rawuin = re.findall(regex, r)
    return rawuin[0]


def chainlist(raw_uin, start=0, num=1):
    '''Retrives the list of solitaires'''
    r = s.get(
        'https://qun.qq.com/cgi-bin/group_chain/chain_list',
        params={
            'gc': raw_uin,
            'start': start,
            'num': num,
            'bkn': _bkn(s.cookies['skey'])
        }
    )
    logging.debug('Requested solitaire URL:%s' % r.url)
    return json.loads(r.text)


def chaininfo(raw_uin, chain_cid, start=0, num=1):
    '''Retrives the detailed info of a solitaire'''
    r = s.get(
        'https://qun.qq.com/cgi-bin/group_chain/chain_get',
        params={
            'gc': raw_uin,
            'cid': chain_cid,
            'get_type': 0,
            'start': start,
            'num': num,
            'bkn': _bkn(s.cookies['skey'])
        }
    )
    return json.loads(r.text)


def chainsignup(raw_uin, chain_cid):
    '''Perform signup'''
    r = s.get(
        'https://qun.qq.com/cgi-bin/group_chain/chain_sign',
        params={
            'gc': raw_uin,
            'cid': chain_cid,
            'bkn': _bkn(s.cookies['skey'])
        }
    )
    return json.loads(r.text)


list_count = 5
chain_member_count = 15

# Match with regex
share_url = re.findall(r'http[s]?:/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',share_url)[0]

rawuin = getRawUin(share_url)
logging.debug('真实群号：%s' % rawuin)
logging.debug('接龙 Web URL：%s' %
              'https://qun.qq.com/homework/qunsolitaire/list.html?gc=' + rawuin)
# List all chains
chains = chainlist(rawuin, 0, list_count)
userio.listout(chains['data']['list'], foreach=lambda x,
               i: f"{x['name']}:{x['desc']}", title=f'接龙详情（最近 {list_count} 次）', reverse=True)

for chain in chains['data']['list']:
    # Perform the followings to every chain in list
    time.sleep(1)

    chain_info = chaininfo(rawuin, chain['id'], 0, chain_member_count)
    print(
        f"准备签到：{chain_info['data']['info']['creater_nick']}:{chain_info['data']['info']['desc']}")

    time.sleep(1)

    userio.listout(chain_info['data']['signup_uins'], foreach=lambda x,
                   i: f"QQ：{str(x['uin']).ljust(15)} | {['','已签到','未签到'][x['type']]} | {x['name']}  {'（我）' if str(x['uin']) in s.cookies['uin'] else ''}", title=f'所有人员（前 {chain_member_count} 位）')

    time.sleep(1)

    # Wait,then try to signup
    try:
        result = chainsignup(rawuin, chain['id'])
        print('结果：', result['msg'] if result['msg'] else '成功')
    except Exception as e:
        logging.error(e)

logging.info('执行完毕')
