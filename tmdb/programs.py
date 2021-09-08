import json
import os
import requests
from tmdb import URLMaker
from dotenv import load_dotenv

# Hide API KEY
# verbose: .env 파일 누락 등의 경고 메시지 출력 옵션
load_dotenv(verbose=True)
TMDB_KEY = os.getenv('TMDB_KEY')
url = URLMaker(TMDB_KEY)

# https://image.tmdb.org/t/p/original

def create_program_genre_data():
    genre_url = url.get_program_genre_url()
    raw_data = requests.get(genre_url)
    json_data = raw_data.json()
    genres = json_data.get('genres')

    genre_data = []

    for genre in genres:
        tmp = {
            'model': 'programs.genre',
            'pk': genre['id'],
            'fields': {
                'name': genre['name']
            }
        }
        genre_data.append(tmp)

    with open('programs.json', 'w', encoding='utf8') as f:
        json.dump(genre_data, f, indent=4)


def create_program_data():
    with open('programs.json', 'r+', encoding='utf-8') as f:
        program_data = json.load(f)
    episode_ids = []

    print('-- TV 프로그램 데이터 작업 시작 --')

    for page in range(1, 501):
        raw_data = requests.get(url.get_program_url(page=page))
        json_data = raw_data.json()
        programs = json_data.get('results')

        for program in programs:
            fields = {}
            fields['poster_path'] = program.get('poster_path')
            fields['name'] = program.get('name')
            fields['original_name'] = program.get('original_name')
            fields['overview'] = program.get('overview')
            fields['popularity'] = program.get('popularity')
            fields['first_air_date'] = program.get('first_air_date')
            fields['vote_average'] = program.get('vote_average')
            fields['vote_count'] = program.get('vote_count')
            fields['origin_country'] = program.get('origin_country')
            fields['like_users'] = []

            # Program detail
            program_id = program.get('id')
            detail_raw_data = requests.get(url.get_program_detail_url(program_id))
            details = detail_raw_data.json()

            fields['seasons'] = details.get('seasons')
            fields['genres'] = details.get('genres')
            fields['number_of_episodes'] = details.get('number_of_episodes')
            fields['number_of_seasons'] = details.get('number_of_seasons')
            fields['seasons'] = details.get('seasons')

            json_model = {
                'model': 'programs.program',
                'pk': program_id,
                'fields': fields,
            }
            program_data.append(json_model)

            '''
            Episodes datas
            시즌 데이터만 넣어도 많기 때문에 우선 건너뛴다
            '''
    with open('programs.json', 'w', encoding='utf-8') as f:
        json.dump(program_data, f, indent=4)

    print('-- TV 프로그램 데이터 작업 완료 --')




if __name__ == '__main__':
    create_program_genre_data()
    create_program_data()
