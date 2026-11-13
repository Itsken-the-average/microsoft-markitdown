# terminal cmd or powershell
# 1 - [ .\.venv\Scripts\Activivate.ps1 ]
# 2 - [ uv run .\main.py ]

from pathlib import Path
from markitdown import MarkItDown

INPUT_FOLDER = Path("documents")
OUTPUT_FOLDER = Path("result")

# File types MarkItDown can handle
SUPPORTED = {
    ".pdf",
    ".docx",
    ".xlsx",
    ".pptx",
    ".html",
    ".htm",
    ".txt",
    ".csv",
    ".json",
    ".xml",
}


def convert_file(md, file_path):
    print(f"Converting {file_path.name}...")
    result = md.convert(str(file_path))

    output_file = OUTPUT_FOLDER / (file_path.stem + ".md")
    output_file.write_text(result.text_content, encoding="utf-8")
    print(f"  Saved to {output_file}")


def main():
    if not INPUT_FOLDER.exists():
        print(
            f"Folder '{INPUT_FOLDER}' not found. Create it and put your files inside."
        )
        return

    OUTPUT_FOLDER.mkdir(exist_ok=True)

    files = [
        f
        for f in INPUT_FOLDER.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED
    ]

    if not files:
        print(f"No supported files found in '{INPUT_FOLDER}'.")
        return

    md = MarkItDown()
    done, failed = 0, 0

    for file_path in files:
        try:
            convert_file(md, file_path)
            done += 1
        except Exception as e:
            print(f"  Failed: {file_path.name} -> {e}")
            failed += 1

    print(f"\nDone. {done} converted, {failed} failed.")


if __name__ == "__main__":
    main()

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
