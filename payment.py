import uuid
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_receipts(data_list, pdf_filename):
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    elements = []
    # Define table data
    table_data = [["Transaction ID", "Customer Name",
                 "Transaction Type", "Amount", "Date"]]
    for data in data_list:
        table_data.append([data["transaction_id"], data["customer_name"],
                          data["transaction_type"], f"${data['amount']:.2f}", data["date"]])

    # Create table and set style
    table = Table(table_data, colWidths=[120, 180, 120, 80, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)
    print(f"Receipts saved as '{pdf_filename}'")


def main():
    num_receipts = int(input("Enter the number of receipts: "))
    data_list = []

    for i in range(num_receipts):
        customer_name = input(f"Enter customer name for receipt {i+1}: ")
        transaction_type = input(f"Enter transaction type for receipt {i+1}: ")
        amount = float(input(f"Enter amount for receipt {i+1}: "))
        date = input(f"Enter date of transaction for receipt {i+1}: ")

        # Generating a random 8-character transaction ID
        transaction_id = str(uuid.uuid4())[:8]

        data_list.append({
            "transaction_id": transaction_id,
            "customer_name": customer_name,
            "transaction_type": transaction_type,
            "amount": amount,
            "date": date
        })

    pdf_filename = input("Enter PDF filename: ")
    generate_receipts(data_list, pdf_filename)

if _name_ == "_main_":
    main()