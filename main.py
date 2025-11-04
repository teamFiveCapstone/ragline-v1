from docling.document_converter import DocumentConverter
from langchain.text_splitter import RecursiveCharacterTextSplitter

def main():
    pdf_path = "lion-quick-guide.pdf"
    output_path = "lion-quick-guide-chunks.txt"

    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    text = result.document.export_to_markdown()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = splitter.split_text(text)

    with open(output_path, "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks, start=1):
            f.write(f"--- Chunk {i} ---\n")
            f.write(chunk + "\n\n")

    print(f"Done! {len(chunks)} chunks saved in '{output_path}'.")

if __name__ == "__main__":
    main()
