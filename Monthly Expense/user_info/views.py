from django.shortcuts import render

def show_user_info(request):

    if request.method == 'POST':
        user_name = request.POST["user_name"]
        return render(request, 'user_info/user_info.html', {'name':user_name})

    return render(request, 'user_info/user_info.html')
