from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.models import User
from userProfile.models import ProfileDetails
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            auth_login(request, user)

            profile_details_queryset = ProfileDetails.objects.filter(user=request.user)

            if profile_details_queryset.exists():
                profile_details = profile_details_queryset.last()  # Use the last instance
            else:
                # Create a new ProfileDetails instance if none exists
                profile_details = ProfileDetails.objects.create(user=request.user)

            # Return relevant user information including ProfileDetails
            response_data = {
                "status": True,
                "message": "Login sukses!",
                "user": {
                    "id": user.id,
                    "username": user.username,
                },
                "profile_details": {
                    "bio": profile_details.bio,
                    "image": profile_details.image.url if profile_details.image else None,
                },
            }

            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali username atau kata sandi."
        }, status=401)
            
    
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": False, "message": "Username already used."}, status=400)

        if password != confirm_password:
            return JsonResponse({"status": False, "message": "Password and confirm password do not match."}, status=400)

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return JsonResponse({"username": user.username, "status": True, "message": "Register successful!"}, status=201)
    else:
        return JsonResponse({"status": False, "message": "Invalid request method."}, status=400)