import json
import os
import requests
from tmdb import URLMaker
from dotenv import load_dotenv
import pandas as pd

# Hide API KEY
# verbose: .env 파일 누락 등의 경고 메시지 출력 옵션
load_dotenv(verbose=True)
# TMDB_KEY = os.getenv('TMDB_KEY')        # "export TMDB_KEY=(발급 받은 api key)" 로 key를 환경 변수로 추가 해주어야 한다.

TMDB_KEY = 'ce028cad82d684aa4fb7bed674115688'

url = URLMaker(TMDB_KEY)

def create_movie_review_data():
    
    # 영화 ID 리스트를 불러오기 위해, 이전에 만든 movies.json을 가져온다.
    with open('movies.json','r') as f:
        data = json.loads(f.read())
    df_nested_list = pd.json_normalize(data)
    
    print(TMDB_KEY)

    review_data = []
    index = 0
    # 각 영화마다 해당하는 리뷰를 가져온다.
    for movie_id in df_nested_list['pk']:  
        if index == 100:
            break
        index = index + 1 
         # print(movie_id)
        review_url = url.get_movie_review_url(movie_id = movie_id, page = 1)
        raw_data = requests.get(review_url)
        json_data = raw_data.json()
        reviews = json_data.get('results')

        # 여러 리뷰 중, 리뷰 하나 씩을 가져온다.
        for review in reviews:
            # 리뷰 중, rating을 작성하지 않은 리뷰는 생략한다.
            if review['author_details']['rating'] == None:
                continue

            tmp = {
                'userId': review['id'],
                'movieId': movie_id,
                'rating': review['author_details']['rating'],

            }
            # print(tmp)
            review_data.append(tmp)     # 리뷰를 담는다.

    # 모두 담긴 리뷰를 movie_reviews.json으로 만든다.
    with open('movie_reviews.json', 'w') as f:
        json.dump(review_data, f, indent=4)

    pass

if __name__ == '__main__':
    create_movie_review_data()
