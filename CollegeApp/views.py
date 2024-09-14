from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

# from some_module_for_text_extraction import extract_text 
import pytesseract
from PIL import Image
import os

# Create your views here.

def college(request):
    return render(request , 'college.html')

def home(request):
    return render(request , 'home.html')

def About(request):
    return render(request , 'about.html')

def  services(request):
    return render(request , 'services.html')

def contact(request):
    return render(request , 'contact.html')

def Scan(request):
    return render(request , 'Scan.html')


def upload_and_scan_image(request):
    if request.method == 'POST':
        # Handle file upload and scanning here
        # Return some mock data for now
        return JsonResponse({'extracted_text': 'Some harmful ingredients detected!'})
    return render(request, 'upload_and_scan.html')

def upload_file(request):
    extracted_text = None  # Initialize variable
    if request.method == 'POST' and request.FILES['document']:
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(file_name)
        
        # Extract text from the uploaded file
        # extracted_text = extract_text(fs.path(file_name))  # This function extracts text from the file

    return render(request, 'upload.html', {
        'file_url': file_url,
        'extracted_text': extracted_text,
    })
