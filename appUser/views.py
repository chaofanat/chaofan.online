from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import Profile
from django.shortcuts import get_object_or_404
@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'account/profile.html',{'profile':profile})


#JsonResponse
from django.http import JsonResponse
import json
def profile_edit(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body.decode('utf-8'))
            bio = data.get('bio')
            website = data.get('website')

            try:
                profile = Profile.objects.get(user=request.user)
                profile.bio = bio
                profile.website = website
                profile.save()
                return JsonResponse({'success': True})
            except Profile.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Profile does not exist'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
