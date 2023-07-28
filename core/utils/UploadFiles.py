from django.shortcuts import render
from django.http import HttpResponse
from .UploadFiles import extract_emails_from_content

def upload_file_view(request):
    if request.method == 'POST' and request.FILES.get('uploaded_file'):
        uploaded_file = request.FILES['uploaded_file']

        content = uploaded_file.read().decode('utf-8')

        email_list = extract_emails_from_content(content)

        return HttpResponse(f"Extracted emails: {', '.join(email_list)}")
    else:
        return render(request, 'upload_file.html')