from docling.document_converter import DocumentConverter

source = "/Users/f/Desktop/elephant.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)


elephant_md = result.document.export_to_markdown() #  pdf to markdown 
with open("elephant.md", "w", encoding="utf-8") as f:
    f.write(elephant_md )
print("Markdown saved to elephant.md")


# print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]