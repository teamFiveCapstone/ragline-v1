from docling.document_converter import DocumentConverter

source = "/Users/f/Desktop/climbing.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)


climbing_md = result.document.export_to_markdown() #  pdf to markdown 
with open("climbing.md", "w", encoding="utf-8") as f:
    f.write(climbing_md )
    
print("Markdown saved to climbing.md")
