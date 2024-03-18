from django.shortcuts import render, get_object_or_404
from .models import UserModel

def staffs_view(request):
    staffs = UserModel.objects.all()

    context = {
        "staffs": staffs,
    }

    return render(request, "users/staffs.html", context)


def staff_view(request, pk):
    staff = get_object_or_404(UserModel, id=pk)
    edu = staff.edu
    pos = staff.pos

    for _ in staff.EDU_CHOICES:
        if edu in _:
            edu = _[1]

    for _ in staff.POS_CHOICES:
        if pos in _:
            pos = _[1]


    context = {
        "staff": staff,
        "edu": edu,
        "pos": pos,
    }

    return render(request, "users/staff.html", context)
