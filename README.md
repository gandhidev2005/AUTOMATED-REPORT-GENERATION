# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: Dev Nilesh Gandhi

*INTERN ID*: CT04DM1209

*DOMAIN*: Python Programming

*DURATION*: 4 weeks

*MENTOR*: Neela Santhosh Kumar

# 📊 Student Academic Report Generator
This Python project reads student academic data from a CSV file, calculates total scores and summary statistics, and generates a structured PDF report using the FPDF library. It is designed to help educators and administrators efficiently summarize student performance.

## 🚀 Features
* Reads data from a CSV file containing student names and subject scores.
* Automatically calculates the **total score** for each student.
* Generates a PDF report with:
  * Tabular data
  * Individual student scores
  * Summary statistics (average, highest, and lowest total score)
* Produces a clean, printable academic report in PDF format.

## 🧾 CSV File Format
The input CSV file **must not include a `Total` column**. The script calculates totals automatically. It should look like this:
```csv
Name,Math,Science,English
Aarav,85,90,88
Ishita,78,84,80
Rohan,92,88,91
Meera,89,85,87
Kabir,76,81,79
Ananya,88,92,90
```
Each row represents a student’s scores in three subjects: Math, Science, and English.

## 🛠️ Requirements
* Python 3.x
* `fpdf` for PDF generation
Install dependencies with:
```bash
pip install fpdf
```

## 🧠 How It Works

### 1. **Read Data**
The `read_student_data(file_path)` function:
* Opens the CSV file.
* Reads each row using `csv.DictReader`.
* Converts each subject score to an integer.
* Dynamically calculates the total score for each student.

### 2. **Generate Report**
The `generate_pdf_report(students, output_path)` function:
* Uses `FPDF` to create a new PDF.
* Adds a title and table headers.
* Lists each student’s name, scores, and calculated total.
* Calculates and displays:
  * Average total score
  * Highest total score
  * Lowest total score

## 📂 File Paths
Make sure to update the script with the correct paths to your CSV and output PDF:
```python
csv_path = r"C:\Path\To\student_scores.csv"
pdf_path = r"C:\Path\To\student_report.pdf"
```

## 🖨️ Output PDF Includes
* Title: **"Student Academic Report"**
* Table with each student’s scores and calculated total
* Summary section:
  * **Average Total Score**
  * **Highest Total Score**
  * **Lowest Total Score**

## 🔧 Possible Improvements
* Add support for more subjects.
* Add student grade categories (A, B, C, etc.).
* Export statistics to Excel.
* Integrate with a web UI for uploads and downloads.
