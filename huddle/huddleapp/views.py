from django.shortcuts import render, get_object_or_404
from huddleapp.models import Post
from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.core import serializers

# Create your views here.
def index(request):
    context = {}
    return render(request, 'huddleapp/index.html', context)

def post(request):
    # TODO: Error handling
    post = Post(title = request.POST["title"], body = request.POST["body"],
                author = "Anonymous", pub_date = timezone.now())
    post.save()
    return HttpResponse(post)

def posts(request):
    latest_posts = serializers.serialize("json",
                                         Post.objects.order_by("-pub_date"))
    return JsonResponse(latest_posts, safe=False)

def postDetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_serialized = serializers.serialize("json", [post, ])
    return JsonResponse(post_serialized, safe=False)

