from django.shortcuts import render
import pdfplumber

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        pdf = request.FILES.get("pdf")
        context["text"] = plum_daldal(pdf)
    return render(request, "pread/index.html", context)

def plum_daldal(filename):
    st = ""
    with pdfplumber.open(filename) as pdf:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            st += page.extract_text()
    return st
