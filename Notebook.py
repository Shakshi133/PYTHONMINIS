from fpdf import FPDF
import pandas as pd

# Initialize PDF
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Load the topics CSV
df = pd.read_csv("Notebook.csv")

# Iterate through each topic
for index, row in df.iterrows():
    # First page for the topic
    pdf.add_page()

    # Header
    pdf.set_font(family="Courier", style="B", size=20)
    pdf.set_text_color(0, 0, 139)  # Dark Blue
    pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1)
    pdf.set_draw_color(100, 100, 100)  # Optional: dark blue line to match heading
    pdf.line(x1=10, y1=pdf.get_y() + 1, x2=200, y2=pdf.get_y() + 1)

    # Footer
    pdf.ln(265)
    pdf.set_font(family="Courier", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Additional pages (if any)
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Header (optional: repeat on each page)
        pdf.set_font(family="Courier", style="B", size=20)
        pdf.set_text_color(0, 0, 139)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1)
        pdf.set_draw_color(100, 100, 100)  # Optional: dark blue line to match heading
        pdf.line(x1=10, y1=pdf.get_y() + 1, x2=200, y2=pdf.get_y() + 1)


        # Footer
        pdf.ln(265)
        pdf.set_font(family="Courier", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# Save the PDF
pdf.output("output.pdf")
