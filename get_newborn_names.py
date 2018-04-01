import requests


def get_new_born_names(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('Что то пошло не так')
if __name__ == '__main__':
    data = get_new_born_names('https://apidata.mos.ru/v1/datasets/2009/rows?api_key=c2d33ae9cb563b3664b30f55149e1934')
    print(data)