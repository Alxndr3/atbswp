import requests

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
# print(res.status_code)
# print(res.status_code == requests.codes.ok)
# print(len(res.text))
# print(res.text[:250])

# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# try:
#    res.raise_for_status()
# except Exception as exc:
#    print(f'There was a problem: {exc}')

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
with open('romeu_and_juliet', 'wb') as play_file:
    for chunk in res.iter_content(100000):
        play_file.write(chunk)
