import requests
import json
import re
import logging,coloredlogs

from myutils import userio,urlparams
coloredlogs.install(logging.DEBUG)
cookies = """
pgv_pvid=2986671978; pgv_pvi=7280240640; RK=Ek5xPVJGUE; ptcz=ba448e2788d8d4dc443714d7d0b69cdce7a705b93715c21fc280b6036f768056; tvfe_boss_uuid=78e57206f6625467; ts_refer=ADTAGCLIENT.QQ.5603_.0; ts_uid=6431297639; eas_sid=h1D5U8f3E7H6B242P5M659D3s1; ptui_loginuin=2949306730; luin=o2949306730; lskey=00010000a0631c67cd3e5ba8eb70ffa787f9d6c38048442c5c0d49e7d69044a156d7dec8a59442e215aa5d20; pgv_si=s3977101312; _qpsvr_localtk=0.5601014086081146; uin=o2137923739; skey=@uZANbhKgr; p_uin=o2137923739; pt4_token=VpHLrHlpKTmdGG-Faf1CuRIT2Yi4aFZ7MzsA4jpI39I_; p_skey=d9WBsgaVocBCV5eGBIKIEfmrbmvxB3-UYcuqms9Kp*k_; traceid=2f5523deb0; pgv_info=ssid=s9277498560; idqq_account=theCanChange%3D1%3BtheShowUin%3D2137923739%3BBindedPhone%3D133******86%3BPhoneCanSeach%3D1%3Bmb%3D180******60%3BUinCanSeach%3D1%3Bshouldshowmail%3D1%3Bfirstsetidqq%3D1%3BMSK%3D0%3B
"""


def _bkn(skey):
    '''bkn:for csrf token'''
    mask1, mask2 = 5381, 0x7FFFFFFF
    # ‭1 0101 0000 0101‬ and ‭111 1111 1111 1111 1111 1111 1111 1111‬
    for char in skey:
        mask1 = mask1 + ((mask1 << 5) + ord(char))
    return mask1 & mask2


cookies =  urlparams.GetParams(cookies)
s = requests.Session()
s.cookies.update(cookies)

def getRawUin(share_url):
    '''Fetches real ID of `QQqun`'''
    regex = '(?<=rawuin = )\d*'
    r = s.get(share_url).text
    rawuin = re.findall(regex,r)
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
    return json.loads(r.text)

def chaininfo(raw_uin,chain_cid, start=0, num=1):
    '''Retrives the detailed info of a solitaire'''
    r = s.get(
        'https://qun.qq.com/cgi-bin/group_chain/chain_get',
        params={
            'gc': raw_uin,
            'cid':chain_cid,
            'get_type':0,
            'start': start,
            'num': num,
            'bkn': _bkn(s.cookies['skey'])
        }
    )    
    return json.loads(r.text)

share = 'https://jq.qq.com/?_wv=1027&k=55gKUHM'

rawuin = getRawUin(share)
logging.debug('真实群号：%s' % rawuin)

chains = chainlist(rawuin)
userio.listout(chains['data']['list'],foreach=lambda x,i:f"{x['name']}:{x['desc']}",title='接龙详情')
