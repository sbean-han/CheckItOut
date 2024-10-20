import json
import requests
from naverbandapi.client import BandOpenApi
from urllib import request

class CIOBandToken:
    token = 'ZQAAAXGiKTyGNuCdE77hKvr9_lELYlrnntxypBloeQDh6-UqVRioF-MWU31X-vMlpLzCtggDEi0ciG9ibJnkwkoOmgg3mlKwRaOQ3Go6rZJU6Bx_'# 한수빈Token임. 개인정보 조회하면 한수빈으로 나옴
    client_id= '43936540'
    redirect_uri='http://localhost:8888'
    client_secret='mebdlfZfOzbicInuZHp15mORFL8TFUL0'
    bandkey='AAAEXPSpQDly5hUs9Q5RUmv0'

def get_reviews() ->list:
    CIOBandAPI=BandOpenApi(CIOBandToken.token)
    reviews=[]
    response=CIOBandAPI.get_posts(CIOBandToken.bandkey, "ko_KR")
    while 'items' in response:
        for it in response['items']:
            reviews.append(it)
        params=response['paging']['next_params']
        response=CIOBandAPI.get_nextpage('posts', params, 'v2')
    return reviews

def reviews_tojson(reviews):
    with open('reviews.json','w',encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False)