from scraper import get_pdf_links
from download import download_pdfs
from compress import compress_files

def main():
    print("Obtendo links dos PDFs...")
    pdf_links = get_pdf_links()

    if not pdf_links:
        print("Nenhum PDF encontrado.")
        return

    print("Baixando PDFs...")
    downloaded_files = download_pdfs(pdf_links)

    if downloaded_files:
        print("Compactando arquivos...")
        compress_files(downloaded_files)

if __name__ == "__main__":
    main()