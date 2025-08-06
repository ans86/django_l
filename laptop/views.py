from django.shortcuts import render, redirect, get_object_or_404
from laptop.models import Laptop


# ✅ Add Laptop
def laptop(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        details = request.POST.get('details')
        generation = request.POST.get('generation')
        ram = request.POST.get('ram')
        ssd = request.POST.get('ssd')

        if not name or not details or not generation or not ram or not ssd:
            return render(request, 'laptop_form.html', {
                'message': 'Please fill in all required fields.'
            })

        laptop_obj = Laptop(
            name=name,
            image=image,
            details=details,
            generation=generation,
            ram=ram,
            ssd=ssd,
        )
        laptop_obj.save()
        return render(request, 'laptop_form.html', {'message': 'Form submitted successfully!'})

    return render(request, 'laptop_form.html')


# ✅ List Laptops
def laptop_list(request):
    laptops = Laptop.objects.all().order_by('-timeStamp')
    return render(request, 'laptops.html', {'laptops': laptops})


# ✅ Laptop Detail View
def laptop_detail(request, id):
    laptop_detail = get_object_or_404(Laptop, id=id)
    return render(request, 'laptop_detail.html', {'laptop_detail': laptop_detail})


# ✅ Edit Laptop
def laptop_edit(request, id):
    laptop = get_object_or_404(Laptop, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        details = request.POST.get('details')
        generation = request.POST.get('generation')
        ram = request.POST.get('ram')
        ssd = request.POST.get('ssd')

        # Validate important fields
        if not name or not details or not generation or not ram or not ssd:
            return render(request, 'laptop_edit.html', {
                'laptop': laptop,
                'error': 'Please fill in all fields.'
            })

        # Update fields
        laptop.name = name
        laptop.details = details
        laptop.generation = generation
        laptop.ram = ram
        laptop.ssd = ssd

        if image:
            laptop.image = image

        laptop.save()
        return redirect('laptop_detail', id=laptop.id)

    return render(request, 'laptop_edit.html', {'laptop': laptop})


# ✅ Delete Laptop
def laptop_delete(request, id):
    laptop = get_object_or_404(Laptop, id=id)
    laptop.delete()
    return redirect('laptops')  # Assuming your laptop list view is named 'laptops'
