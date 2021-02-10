#!/usr/bin/env python3

# Using reportlab modules to generate the PDF
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Function to generate a basic PDF report to tell the user the data was processed. 
def generate_report(filename, title, info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(info, styles["BodyText"])
    empty_line = Spacer(1,20)
    # Build the report
    report.build([report_title, empty_line, report_info, empty_line])
