# terminal cmd or powershell
# 1 - [ .\.venv\Scripts\Activivate.ps1 ]
# 2 - [ uv run .\main.py ]

from pathlib import Path
from markitdown import MarkItDown

OUTPUT_FOLDER = "result"


def convert_to_markdown(file_path):
    md = MarkItDown()

    print(f"Converting {file_path}...")
    result = md.convert(file_path)

    # Make the result folder if it doesn't exist
    Path(OUTPUT_FOLDER).mkdir(exist_ok=True)

    # Same name as the source, but .md, inside result/
    output_file = Path(OUTPUT_FOLDER) / (Path(file_path).stem + ".md")
    output_file.write_text(result.text_content, encoding="utf-8")

    print(f"Saved successfully to {output_file}")


if __name__ == "__main__":
    # Change this to any file you want to convert
    sample_file = "documents/INTEGRATION-OF-ANALYTICS-ON-PM-IN-IT-ORGANIZATIONS.pdf"

    try:
        convert_to_markdown(sample_file)
    except FileNotFoundError:
        print(f"File not found: '{sample_file}'")
      

""" [new files arrangement]
your-project/
├── main.py
├── documents/        <- put all your source files here
│   ├── myLibro_SRS.pdf
│   └── notes.docx
└── result/           <- all .md files appear here
    ├── myLibro_SRS.md
    └── notes.md

"""



"""
[first version from youtube]
[i have problems when it comes to directory]


from markitdown import MarkItDown


def convert_to_markdown(file_path):
    # Initialize the MarkItDown converter
    md = MarkItDown()

    print(f"Converting {file_path}...")
    # Perform the conversion
    result = md.convert(file_path)

    # Print the text content
    print("\n--- Conversion Result ---\n")
    print(result.text_content)

    # Save to a file
    output_file = file_path.rsplit(".", 1)[0] + ".md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result.text_content)
    print(f"\nSaved successfully to {output_file}")


if __name__ == "__main__":
    # Replace this with any local docx, xlsx, pptx, pdf, or html file
    sample_file = "documents/myLibro_SRS.pdf"

    try:
        convert_to_markdown(sample_file)
    except FileNotFoundError:
        print(f"Please place '{sample_file}' in this directory to test.")
        """
