def siteChecKer(url):
    import requests

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Obtemos o nome do site pela ur informada 
        nome_site = response.url
        status_site = '\033[32mDISPONIVEL\033[0m'

        return nome_site, status_site
    
    except requests.exceptions.RequestException:
        return url, f'\033[31mINDISPONIVEL\033[0m'
    



print('=' * 62)
print('\033[33mSITE CHECKER 0.1.1\033[0m'.center(62))
print('=' * 62)

url = input('Informe a url: ')

nome_site, status_site = siteChecKer(url)

print('-' * 62)
print(f'Site: \033[34m{nome_site}\033[0m')
print(f'Status site: {status_site}')
print('-' * 62)
print('=' * 62)
print('\033[33mVOLTE SEMPRE QUE PRECISAR!\033[0m'.center(62))
print('=' * 62)
