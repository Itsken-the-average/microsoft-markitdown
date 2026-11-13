# terminal cmd or powershell
# 1 - [ .\.venv\Scripts\Activate.ps1 ]
# 2 - [ uv run .\main.py ]

import re
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from markitdown import MarkItDown

OUTPUT_FOLDER = "result"
INPUT_FOLDER = "documents/"


def is_url(source):
    return source.startswith(("http://", "https://"))


def get_output_name(source):
    """Same name as the source (for files) or the video ID (for URLs)."""
    if not is_url(source):
        return Path(source).stem

    url = urlparse(source)

    # youtu.be/VIDEO_ID
    if "youtu.be" in url.netloc:
        return url.path.strip("/")

    # youtube.com/watch?v=VIDEO_ID
    video_id = parse_qs(url.query).get("v")
    if video_id:
        return video_id[0]

    # Any other website: clean up the address so it's a safe file name
    return re.sub(r"[^A-Za-z0-9_-]", "_", url.netloc + url.path).strip("_")


def convert_to_markdown(source):
    md = MarkItDown()

    print(f"Converting {source}...")
    result = md.convert(source)

    Path(OUTPUT_FOLDER).mkdir(exist_ok=True)

    output_file = Path(OUTPUT_FOLDER) / (get_output_name(source) + ".md")
    output_file.write_text(result.text_content, encoding="utf-8")

    print(f"Saved successfully to {output_file}")


if __name__ == "__main__":
    # OPTION 1: a file inside documents/
    # sample_file = INPUT_FOLDER + "myLibro_SRS.pdf"

    # OPTION 2: a YouTube link or website (no folder in front!)
    sample_file = "https://youtu.be/8mN16cORwkc?si=7iXyZv-7XhdiqFBc"

    try:
        convert_to_markdown(sample_file)
    except FileNotFoundError:
        print(f"File not found: '{sample_file}'")
    except Exception as e:
        print(f"Failed: {e}")    

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
