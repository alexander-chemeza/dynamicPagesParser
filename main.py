import json
from get_pages import get_pages
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # Initialize dictionary, string, domain address
    articles_data = {}
    src = ''
    domain = 'https://cars.av.by'

    # Get pages elements
    pages = get_pages('https://cars.av.by/filter?brands[0][brand]=683&page=', 'listing-item')

    # Convert pages into single string
    for item in pages:
        src += str(item)

    # Get list of elements
    articles_soup = BeautifulSoup(src, 'lxml')
    articles_list = articles_soup.findAll('div', class_='listing-item')

    # Build dictionary to write as JSON
    for article in articles_list:
        article_about = article.find('div', class_='listing-item__wrap').find('div', class_='listing-item__about').find(
            'h3').find('a')
        article_params = article.find('div', class_='listing-item__wrap').find('div', class_='listing-item__params').findChildren()

        title = article_about.find('span').text
        title_year = article_params[0].text
        title_params = article_params[1].text
        title_mileage = article_params[2].text
        title_price = article.find('div', class_='listing-item__wrap').find('div', class_='listing-item__prices').find(
            'div', class_='listing-item__price').text
        title_url = domain + article_about.get('href')
        title_number = title_url.split('/')[5]

        articles_data[title_number] = {
            "title": title,
            "year": title_year,
            "about": title_params,
            "mileage": title_mileage,
            "price": title_price,
            "url": title_url
        }

    # Save to JSON file
    with open('mercedes.json', 'w', encoding='utf-8') as file:
        json.dump(articles_data, file, indent=4, ensure_ascii=False)

