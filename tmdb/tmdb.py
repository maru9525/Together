import requests
import json


class URLMaker:
    url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def get_movie_genre_url(self):
        url = f'{self.url}/genre/movie/list?api_key={self.key}'
        return url

    def get_movie_url(self, category='movie', feature='popular', page='1'):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}&language=ko-KR&page={str(page)}'
        return url

    def get_program_genre_url(self):
        url = f'{self.url}/genre/tv/list?api_key={self.key}'
        return url

    def get_program_url(self, category='tv', feature='popular', page='1'):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}&language=ko-KR&page={str(page)}'
        return url

    def get_program_detail_url(self, program_id):
        url = f'{self.url}/tv/{program_id}'
        url += f'?api_key={self.key}&language=ko-KR'
        return url

    # def get_program_episode_group_url(self, program_id):
    #     url = f'{self.url}/tv/{program_id}/episode_groups'
    #     url += f'?api_key={self.key}&language=ko-KR'
    #     return url

    # def get_program_episode_group_details_url(self, episode_group_id):
    #     url = f'{self.url}/tv/episode_group/{episode_group_id}'
    #     url += f'?api_key={self.key}&language=ko-KR'
    #     return url
