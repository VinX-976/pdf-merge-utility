from pypdf import PdfReader, PdfWriter
from pathlib import Path


def merge_pdfs(
    input_paths: list[Path],
    output_path: Path,
    overwrite: bool = False
) -> None:
    """
    Merge multiple PDF files into a single PDF file
    Checks on input files, output file and output directory enforce the universality of this helper 

    :param input_files: List of paths to PDF files
    :param output_file: Output PDF path
    """

    # Check if files are provided
    if not input_paths:
        raise ValueError("No input files provided.")
    
    # Check parent directory exists
    if not output_path.parent.exists():
        raise FileNotFoundError(
            f"Output directory does not exist: {output_path.parent}"
        )

    # Prevent overwrite
    if output_path.exists() and not overwrite:
        raise FileExistsError(
            f"Output file already exists: {output_path}"
        )
    
    # Validate input paths
    for input_path in input_paths:
        
        if not input_path.exists():
            raise FileNotFoundError(f"File not found: {input_path}")
        
        if input_path.suffix.lower() != ".pdf":
            raise ValueError(f"Not a PDF file: {input_path}")
    
    writer = PdfWriter()

    # Merging
    for input_path in input_paths:
        
        reader = PdfReader(str(input_path))

        for page in reader.pages:
            writer.add_page(page)

    # Write the merged file
    with open(output_path, "wb") as f:
        writer.write(f)

