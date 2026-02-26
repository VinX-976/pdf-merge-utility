from pathlib import Path

def normalize_paths(input_paths: list[str | Path], output_path: str | Path) -> tuple[list[Path], Path]:
    # convert all inputs to Path objects
    input_paths = [Path(p) if not isinstance(p, Path) else p for p in input_paths]
    output_path = Path(output_path) if not isinstance(output_path, Path) else output_path

    return (input_paths, output_path)