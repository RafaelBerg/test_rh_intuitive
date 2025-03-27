from scraper import get_pdf_links
from download_pdf import download_pdf
from download_ans import download_ans
from compress import compress_files

def main():
    print("Obtendo links dos PDFs...")
    pdf_links = get_pdf_links()

    if not pdf_links:
        print("Nenhum PDF encontrado.")
        return

    print("Baixando PDFs...")
    downloaded_files = download_pdf(pdf_links)

    if downloaded_files:
        print("Compactando arquivos...")
        compress_files(downloaded_files)
        
    print("Baixando arquivos ANS...")
    download_ans()

if __name__ == "__main__":
    main()