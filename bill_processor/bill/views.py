from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import cv2
import re
from openpyxl import Workbook, load_workbook
import os
import easyocr
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        # Delete previous uploaded file if exists
        if 'uploaded_file_url' in request.session:
            previous_file_path = os.path.join(settings.MEDIA_ROOT, request.session['uploaded_file_url'])
            if os.path.exists(previous_file_path):
                os.remove(previous_file_path)

        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)

        # Store the uploaded file URL in session to keep track of it
        request.session['uploaded_file_url'] = filename

        # Process the image and extract data
        process_image(fs.path(filename))

        return render(request, 'bill_detail.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'bill_detail.html')

def process_image(image_path):
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply some preprocessing (optional but can improve OCR accuracy)
    _, processed_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Perform OCR on the processed image
    result = reader.readtext(processed_image, detail=0)

    # Join the result into a single string
    text = " ".join(result)

    # Print the OCR result to verify
    print("OCR Text:", text)

    # Tokenize text using NLTK
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Join filtered tokens back into a string
    filtered_text = " ".join(filtered_tokens)

    # Print the filtered OCR text
    print("Filtered OCR Text:", filtered_text)

    # Define regex patterns for specific fields
    address_pattern = re.compile(r'Name and Address: ([\w\s,]+)')
    rr_pattern = re.compile(r'RR Number \$?(\d+\.?\d+[A-Za-z]*)')
    acc_pattern = re.compile(r'Account ID \$?(\d+\.?\d*)')
    amt_pattern = re.compile(r'Due\s*:\s*(\d+\s\d+\s[\d.]+)')
    consume_pattern = re.compile(r'Consumption \$?(\d+\.?\d*)')
    tax_pattern = re.compile(r'Tax \$?(\d+\.?\d*)')
    date_pattern = re.compile(r'J8637\s*Uc=\s*Reading Date:\s*(\d{2})\s*/\s*(\d{2})\s*/\s*(\d{2})')

    # Search for patterns in OCR text
    address = address_pattern.search(filtered_text)
    rr = rr_pattern.search(filtered_text)
    accoun = acc_pattern.search(filtered_text)
    amt = amt_pattern.search(filtered_text)
    consume = consume_pattern.search(filtered_text)
    tax = tax_pattern.search(filtered_text)
    date = date_pattern.search(filtered_text)

    # Print the matches to verify
    print("Address Match:", address.group(1) if address else "No match")
    print("RR Number:", rr.group(1) if rr else "No match")
    print("Reading Date:", date.group(0) if date else "No match")
    print("Account ID Match:", accoun.group(1) if accoun else "No match")
    print("Consumption Match:", consume.group(1) if consume else "No match")
    print("Tax Match:", tax.group(1) if tax else "No match")
    print("Net Amount Due Match:", amt.group(1) if amt else "No match")


    # Check if the Excel file already exists
    excel_path = os.path.join(settings.MEDIA_ROOT, 'bill.xlsx')
    try:
        wb = load_workbook(excel_path)
        ws = wb.active
    except FileNotFoundError:
        wb = Workbook()
        ws = wb.active
        ws.title = 'Bill Information'
        # Write headers if creating a new workbook
        ws['A1'] = 'Name'
        ws['B1'] = 'RR Number'
        ws['C1']='Date'
        ws['D1'] = 'Account ID'
        ws['E1'] = 'Consumption'
        ws['F1'] = 'Tax'
        ws['G1'] = 'Net Amount Due'

    # Determine the next row to write data
    next_row = ws.max_row + 1

    # Write data if found
    if address:
        ws[f'A{next_row}'] = address.group(1)
    if rr:
        ws[f'B{next_row}'] = rr.group(1)
    if date:
        ws[f'C{next_row}'] = date.group(1)
    if accoun:
        ws[f'D{next_row}'] = accoun.group(1)
    if consume:
        ws[f'E{next_row}'] = consume.group(1)
    if tax:
        ws[f'F{next_row}'] = tax.group(1)
    if amt:
        ws[f'G{next_row}'] = amt.group(1)

    # Save the workbook
    wb.save(excel_path)
    print(f"Workbook saved at {excel_path}")
