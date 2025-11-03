from docling.document_converter import DocumentConverter

source = "/Users/f/Desktop/lion.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)


lionPDF_md = result.document.export_to_markdown() #  pdf to markdown 


# code to create md file for output 
with open("lion.md", "w", encoding="utf-8") as f:
    f.write(lionPDF_md )
print("Markdown saved to lion.md")


# print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]