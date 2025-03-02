import requests

def search_unogs(query, audio="English [Original]", limit=20, offset=0, countrylist='21,23,26,29,33,36,307,45,39,327,331,334,265,337,336,269,267,357,378,65,67,390,392,268,400,408,412,447,348,270,73,34,425,432,436,46,78', start_year=1900, end_year=2025):
    headers = {
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MDkyMDIzMiwianRpIjoiNjI4NmE5MGYtYzlhOC00NDIyLTk1ODctNDgyZTUwMTI1ZWQwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjE3NDA5MjAyMzMuMjAyIiwibmJmIjoxNzQwOTIwMjMyLCJleHAiOjE3NDEwMDY2MzJ9.Mq3_uclP1ersmfgsy1w9x76BHhPav1iPpHIZRjA-MWM",
        "referer": "https://unogs.com/search/El?country_andorunique=or&start_year=1900&end_year=2025&end_rating=10&genrelist=&audio=Spanish%20(Latin%20America)%20[Original]&audiosubtitle_andor=or&countrylist=21,23,26,29,33,36,307,45,39,327,331,334,265,337,336,269,267,357,378,65,67,390,392,268,400,408,412,447,348,270,73,34,425,432,436,46,78",
        "referrer": "http://unogs.com",
    }
    url = "https://unogs.com/api/search"
    params = {
        'limit': limit,
        'offset': offset,
        'query': query,
        'countrylist': countrylist,
        'country_andorunique': 'or',
        'start_year': start_year,
        'end_year': end_year,
        'start_rating': '',
        'end_rating': '10',
        'genrelist': '',
        'type': '',
        'audio': audio,
        'subtitle': '',
        'audiosubtitle_andor': 'or',
        'person': '',
        'personid': '',
        'filterby': '',
        'orderby': ''
    }
    response = requests.get(url, headers=headers,params=params)
    return response.json()


def search_with_results(query, audio="English [Original]", limit=20, offset=0, countrylist='21,23,26,29,33,36,307,45,39,327,331,334,265,337,336,269,267,357,378,65,67,390,392,268,400,408,412,447,348,270,73,34,425,432,436,46,78', start_year=1900, end_year=2025):
    results = search_unogs(query, audio, limit, offset, countrylist, start_year, end_year)
    list_of_titles = []
    for result in results['results']:
        list_of_titles.append(result['title'])

    return list_of_titles

if __name__ == '__main__':
    print(search_with_results('Hello'))
    print(search_with_results(query='Soledad',audio='Spanish (Latin America) [Original]'))