import requests
from bs4 import BeautifulSoup
from config import URL

def get_pdf_links():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Erro ao acessar a página.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=True)

    pdf_links = [link["href"] for link in links if "Anexo" in link.text and link['href'].endswith(".pdf")]
    
    return pdf_links