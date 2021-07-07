from django.shortcuts import render
from .Image_sudoku import run_sudoku
from PIL import Image as im
import os
from os import path
# Create your views here.
from .form import ImageForm

def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            url = os.path.abspath("Image_Sudoku/input_image/input.png/")
            inp_img = run_sudoku(url)
            op_img = im.fromarray(inp_img)
            op_img.save('Image_Sudoku/static/output_image/output.png')
            obj = form.instance
            return render(request, 'index.html', {'obj':obj})
    else:
        urls = [os.path.abspath("Image_Sudoku/static/output_image/output.png"),
                os.path.abspath("Image_Sudoku/input_image/input.png/")]
        for url in urls: 
            if path.exists(url):
                os.remove(url)
        form = ImageForm()
    return render(request, 'index.html',{'form': form})
