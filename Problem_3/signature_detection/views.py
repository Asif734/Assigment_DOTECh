from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Signature
from .forms import SignatureForm
import cv2

def compare_signatures(original_path, uploaded_path):
    # Load images in grayscale
    original = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
    uploaded = cv2.imread(uploaded_path, cv2.IMREAD_GRAYSCALE)

    # Example comparison using Template Matching
    similarity = cv2.matchTemplate(original, uploaded, cv2.TM_CCOEFF_NORMED)
    max_similarity = similarity.max()  # Get the highest similarity score
    return max_similarity > 0.9  # Adjust threshold as needed

def upload_signature(request):
    if request.method == 'POST':
        form = SignatureForm(request.POST, request.FILES)
        if form.is_valid():
            signature = form.save()
            match_result = compare_signatures(
                signature.original_image.path,
                signature.uploaded_image.path
            )
            return JsonResponse({'match': match_result})
    else:
        form = SignatureForm()
    return render(request, 'upload_signature.html', {'form': form})

