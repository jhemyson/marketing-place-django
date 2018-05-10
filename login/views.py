from django.shortcuts import render, render_to_response


def register(request):
    return render_to_response('registration/register.html', {})


def register_success(request):
    pass
