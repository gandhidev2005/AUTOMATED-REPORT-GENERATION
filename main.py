import csv
from fpdf import FPDF
import statistics

# Read and analyze data from the CSV file
def read_student_data(file_path):
    students = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = {
                "Name": row["Name"],
                "Math": int(row["Math"]),
                "Science": int(row["Science"]),
                "English": int(row["English"]),
                "Total": int(row["Total"])
            }
            students.append(student)
    return students

# Generate PDF report
def generate_pdf_report(students, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Student Academic Report", ln=True, align='C')
    pdf.ln(10)

    # Table header
    pdf.set_font("Arial", 'B', 12)
    headers = ["Name", "Math", "Science", "English", "Total"]
    col_widths = [40, 30, 30, 30, 30]
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, border=1)
    pdf.ln()

    # Table rows
    pdf.set_font("Arial", size=12)
    for student in students:
        pdf.cell(col_widths[0], 10, student["Name"], border=1)
        pdf.cell(col_widths[1], 10, str(student["Math"]), border=1)
        pdf.cell(col_widths[2], 10, str(student["Science"]), border=1)
        pdf.cell(col_widths[3], 10, str(student["English"]), border=1)
        pdf.cell(col_widths[4], 10, str(student["Total"]), border=1)
        pdf.ln()

    # Summary statistics
    totals = [s["Total"] for s in students]
    avg_total = statistics.mean(totals)
    max_total = max(totals)
    min_total = min(totals)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, "Summary Statistics", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Average Total Score: {avg_total:.2f}", ln=True)
    pdf.cell(200, 10, f"Highest Total Score: {max_total}", ln=True)
    pdf.cell(200, 10, f"Lowest Total Score: {min_total}", ln=True)

    pdf.output(output_path)
    print(f"PDF report saved to {output_path}")

# Run the functions
csv_path = r"C:\Users\devga\Downloads\student_scores.csv"
pdf_path = r"C:\Users\devga\Downloads\student_report.pdf"

students = read_student_data(csv_path)
generate_pdf_report(students, pdf_path)
