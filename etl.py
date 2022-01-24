import os
import pandas as pd
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup

LINE_NUM_THRESHOLD = 20


def create_uuid(k: int):
    id_str = ''
    for l in [10000, 1000, 100, 10]:
        if k < l:
            id_str += '0'
    id_str += str(k)
    return id_str


def filter_text(text: str) -> str:
    text = text.replace('\n', '')
    if '[DOWNLOAD' in text or '[youtube=' in text:
        return ''
    if 'http' in text:
        print(text)
    return text


def clean_txt(txt_dir_path, filename):
    txt_file_path = f'{txt_dir_path}/{filename}'
    ep_name = filename.replace('.txt', '')
    ep_date = ''
    text = []
    with open(txt_file_path, 'r') as f:
        try:
            transcript_len = len([line for line in f])
        except:
            return None, None, None
        if transcript_len <= LINE_NUM_THRESHOLD:
            return None, None, None
    with open(txt_file_path, 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                ep_date = line.replace('\n', '')
                continue
            text.append(filter_text(line))
    text = '    '.join(text)
    return ep_name, ep_date, text


def txt_to_csv(data_dir, transcript_txt_dir, final_csv_filename):
    txt_dir_path = f'{data_dir}/{transcript_txt_dir}'
    txt_files = os.listdir(txt_dir_path)
    csv_data = []
    id_int = 0
    for filename in txt_files:
        ep_name, ep_date, text = clean_txt(txt_dir_path, filename)
        if ep_name is None:
            continue
        id_str = create_uuid(id_int)
        id_int += 1
        csv_data.append([id_str, ep_name, ep_date, text])
    data_df = pd.DataFrame(csv_data, columns=['ep_id', 'ep_name', 'ep_date', 'simple_text'])
    df_path = f'{data_dir}/{final_csv_filename}.csv'
    data_df.to_csv(df_path, index=False)


def process_text(text):
    text = text.replace('TRANSCRIPT\n', '')
    return text


def save_to_txt(header, metadata, text, transcript_dir_path):
    with open(f'{transcript_dir_path}/{header}.txt', 'w') as f:
        for line in metadata:
            f.write(line + '\n')
        for line in text:
            f.write(line + '\n')


def extract_data_from_url(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.find(id="content")
    header = content.find(class_='entry-title').text
    content = content.find(class_='entry-content')
    paragraphs = content.find_all("p")
    full_text = []
    for p in paragraphs:
        text = p.text
        if text.replace(' ', '').lower() in [''] or ('download episode' in text.lower()):
            continue
        full_text.append(process_text(text))
    metadata = []
    ep_date = url.split('teacherluke.co.uk/')[1][:10]
    ep_date = f'{ep_date.split("/")[0]}/{ep_date.split("/")[1]}/{ep_date.split("/")[2]}'
    metadata.append(ep_date)
    return header, metadata, full_text


def scrape_to_txt(data_dir, transript_txt_dir, url_savename):
    transript_txt_dir_path = f'{data_dir}/{transript_txt_dir}'
    if not os.path.exists(transript_txt_dir_path):
        os.mkdir(transript_txt_dir_path)
    url_df = pd.read_csv(f'{data_dir}/{url_savename}.csv')
    for url in tqdm(url_df.values):
        try:
            url = url[0]
            header, metadata, full_text = extract_data_from_url(url)
            save_to_txt(header, metadata, full_text, transript_txt_dir_path)
        except:
            print(f"url {url} failed scraping :(")


def extract_podcast_urls(transcript_main_url, data_dir, url_savename):
    page = requests.get(transcript_main_url)
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.find(id="content")
    content = content.find(class_='entry-content')
    paragraphs = content.find_all("p")
    urls_to_scrape = []
    for p in paragraphs[1:]:
        urls = p.find_all('a', href=True)
        if len(urls) == 0:
            continue
        for url_raw in urls:
            url_raw_str = str(url_raw)
            url = url_raw_str.split('href')[1].split('"')[1]
            urls_to_scrape.append(url)
    urls_to_scrape = pd.Series(urls_to_scrape)
    urls_to_scrape.to_csv(f'{data_dir}/{url_savename}.csv', index=False)


TRANSCRIPT_MAIN_URL = "https://teacherluke.co.uk/archive-of-episodes-1-149/"
DATA_DIR = 'dataset'
TRASCRIPT_TXT_DIR = 'transcripts_txt'
URL_SAVENAME = "urls_to_scrape"
FINAL_CSV_NAME = 'transcripts'

if __name__ == '__main__':
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
    extract_podcast_urls(TRANSCRIPT_MAIN_URL, DATA_DIR, URL_SAVENAME)
    scrape_to_txt(DATA_DIR, TRASCRIPT_TXT_DIR, URL_SAVENAME)
    txt_to_csv(DATA_DIR, TRASCRIPT_TXT_DIR, FINAL_CSV_NAME)