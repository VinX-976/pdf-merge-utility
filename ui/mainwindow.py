from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from pathlib import Path
from pypdf import PdfReader

from ui.ui_mainwindow import Ui_MainWindow
from services.pdf_merger import merge_pdfs

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Merge PDF files")
        
        self.input_paths = []
        self.output_path = None
        self.last_dir = str(Path.home())
        
        # Signals
        self.addButton.clicked.connect(self.add_files)
        self.moveUpButton.clicked.connect(self.move_up_file)
        self.moveDownButton.clicked.connect(self.move_down_file)
        self.removeButton.clicked.connect(self.remove_file)
        self.outputButton.clicked.connect(self.output_file)
        self.mergeButton.clicked.connect(self.merge_files)

    # Slots
    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select PDF files to merge",
            self.last_dir,
            "PDF Files (*.pdf)"
        )

        if not files:
            return

        self.last_dir = str(Path(files[0]).parent)

        for file in files:
            path = Path(file)

            # Extension check
            if path.suffix.lower() != ".pdf":
                QMessageBox.critical(
                    self,
                    "Invalid File",
                    f"{path.name} is not a .pdf file.\nIt will not be added."
                )
                continue

            # Header check
            try:
                with open(path, "rb") as f:
                    header = f.read(5)
                    if header != b"%PDF-":
                        QMessageBox.critical(
                            self,
                            "Invalid File",
                            f"{path.name} does not contain a valid PDF signature.\nIt will not be added."
                        )
                        continue
            except OSError as e:
                QMessageBox.critical(
                    self,
                    "File Error",
                    f"Cannot open {path.name}.\n{str(e)}"
                )
                continue

            # Parse check (corruption and permission test)
            try:
                reader = PdfReader(path)
                _ = reader.pages

            except PermissionError:
                QMessageBox.critical(
                    self,
                    "Permission Error",
                    f"You do not have permission to read {path.name}."
                )
                continue

            except Exception:
                QMessageBox.critical(
                    self,
                    "Corrupted PDF",
                    f"{path.name} cannot be read or is corrupted."
                )
                continue

            # Avoid duplicates
            if path not in self.input_paths:
                self.input_paths.append(path)
                self.listWidget.addItem(path.name)

    def remove_file(self):
        row = self.listWidget.currentRow()

        if row < 0:
            return  # nothing selected
        
        # Remove item from the UI
        self.listWidget.takeItem(row)

        # Remove from the internal list
        self.input_paths.pop(row)

    def move_up_file(self):
        row = self.listWidget.currentRow()

        if row <= 0:
            return  # first item or nothing selected
        
        # Action on UI
        item = self.listWidget.takeItem(row)
        self.listWidget.insertItem(row - 1, item)
        self.listWidget.setCurrentRow(row - 1)

        # Action on internal list
        self.input_paths[row], self.input_paths[row - 1] = self.input_paths[row - 1], self.input_paths[row]

    def move_down_file(self):
        row = self.listWidget.currentRow()

        if row < 0 or row >= self.listWidget.count() - 1:
            return  # last item or nothing selected
        
        # Action on UI
        item = self.listWidget.takeItem(row)
        self.listWidget.insertItem(row + 1, item)
        self.listWidget.setCurrentRow(row + 1)

        # Action on internal list
        self.input_paths[row], self.input_paths[row + 1] = self.input_paths[row + 1], self.input_paths[row]

    def output_file(self):
        file, _ = QFileDialog.getSaveFileName(
        self,                           # parent window
        "Merged PDF file name",         # dialog title
        self.last_dir,                  # start from the last used directory
        "PDF Files (*.pdf)"             # file filter
        )
        
        if not file:
            return  # user closed dialog

        path = Path(file)

        # Ensure .pdf extension
        if path.suffix.lower() != ".pdf":
            path = path.with_suffix(".pdf")

        # Directory must exist
        if not path.parent.exists():
            QMessageBox.critical(
                self,
                "Invalid Directory",
                "The selected directory does not exist."
            )
            return

        # Write permission check
        try:
            test_file = path.parent / "__write_test.tmp"
            with open(test_file, "wb"):
                pass
            test_file.unlink()
        except OSError:
            QMessageBox.critical(
                self,
                "Permission Error",
                "You do not have permission to write in the selected directory."
            )
            return
        
        # Commit only after validation
        self.output_path = path
        self.last_dir = str(path.parent)    # Store the directory of the last selected file
        self.outputLabel.setText(path.name)

    def merge_files(self):
        if len(self.input_paths) < 2:
            QMessageBox.warning(
                self,
                "Error",
                "Please select 2 or more input files before merging."
            )
            return
        
        if not self.output_path:
            QMessageBox.warning(
                self,
                "Error",
                "No output file selected. Please select an output file before merging."
            )
            return
        
        # Edge case protection: user merge again after a change on the file list and forget to select a new output file
        if self.output_path.exists():
            reply = QMessageBox.question(
                self,
                "Overwrite File?",
                f"The output file '{self.output_path.name}' already exists.\nDo you want to overwrite it?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply != QMessageBox.Yes:
                return

        try:
            merge_pdfs(
                self.input_paths,
                self.output_path,
                overwrite=True  # QFileDialog already manage overwrite decision from user
            )

            QMessageBox.information(self, "Success", "PDF files merged successfully.")

        except FileNotFoundError as e:
            QMessageBox.warning(self, "File Error", str(e))

        except ValueError as e:
            QMessageBox.warning(self, "Validation Error", str(e))

        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error", str(e))

