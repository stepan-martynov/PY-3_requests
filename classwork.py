import requests
import subprocess

API_KEY = "trnsl.1.1.20170402T140528Z.9741d87c67b169b8.498152cdc426431b0befea1aad4cd69c1b358a76"
URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"


def yandex_translate(input_file='texts/DE.txt', to_lang='de'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ? 
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
     """
    with open(input_file, encoding='utf-8') as f:
        text = f.read()

    params = {
        "key": API_KEY,
        "text": text,
        "lang": '{}-ru'.format(to_lang)
    }

    translated_text = ''.join(requests.get(URL, params=params).json()['text'])
    return translated_text


def create_file_translate(output_file, translated_text):
    subprocess.run(['touch', output_file])
    with open(output_file, encoding='utf-8', mode='w') as f:
        f.write(translated_text)


def main():
    input_file = input('Введите имя исходного файла для перевода: ')
    to_lang = input('Введите с какого языка перводим: ')
    translated_text = yandex_translate(input_file, to_lang)
    output_file = input('Введите имя файла: ')
    create_file_translate(output_file, translated_text)


if __name__ == '__main__':
    main()
