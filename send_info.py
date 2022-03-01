import requests

TOKEN = '5108400714:AAHp6JO9AWKpGnAQeAMMrwuExweKtnm0K9Y'
USER = '' # Your telegram id. You can get it with halp second file. 

def send_info_error(info=None,):
    try:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={USER}&text={info}')
    except:
        print('Something went wrong')

send_info_error('Hello word')
