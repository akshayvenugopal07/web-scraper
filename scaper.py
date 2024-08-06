import bs4, requests
import csv

urls = [
    "https://qbdgroup.com/en/", 
    "https://qbdgroup.com/es-es/", 
    "https://qbdgroup.com/en/industries/", 
    "https://qbdgroup.com/en/our-way-of-working/project-management/",
    "https://qbdgroup.com/en/contact/",
    "https://qbdgroup.com/en/services/",
    "https://qbdgroup.com/en/upcoming-events/",
    "https://qbdgroup.com/en/about-qbd/",
    "https://qbdgroup.com/en/privacy-policy/",
    "https://qbdgroup.com/en/sitemap/"
]

with open('word-count.csv', 'w', newline='') as file:

    writer = csv.writer(file)

    field = ["URL", "Count"]
    
    writer.writerow(field)

    for index, url in enumerate(urls):

        response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

        soup = bs4.BeautifulSoup(response.text,'lxml')

        text = soup.body.get_text(' ', strip=True)

        with open("URL-"+str(index)+"-Words.txt", "w") as file:
            
            file.write(str(text.split()))

        print("No of words found in the", url," page was:",len(text.split()))

        writer.writerow([url, len(text.split())])
