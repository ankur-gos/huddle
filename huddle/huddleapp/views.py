from django.shortcuts import render, get_object_or_404
from huddleapp.models import Post, Followup, FollowupComment, PostSerializer
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
    serializer = PostSerializer(instance=post)
    post_serialized = serializers.serialize("json", [post, ])
    return JsonResponse(serializer.data, safe=False)

def followup(request):
    post = get_object_or_404(Post, pk=request.POST["post_id"])
    Followup.objects.create(post = post, author = "Anonymous", followup_text =
                             request.POST["body"], pub_date = timezone.now())

    #post.followups.create(author = "Anonymous", followup_text =
#                             request.POST["body"], pub_date = timezone.now())
    #post_serialized = serializers.serialize("json", [post, ])
    return JsonResponse("", safe=False)

def addStudentEdit(request):
    post = get_object_or_404(Post, pk=request.POST["post_id"])
    post.student_answer = request.POST["body"]
    post.save()
    return JsonResponse("", safe=False)

def followupComment(request):
    followup = get_object_or_404(Followup, pk=request.POST["followup_id"])
    FollowupComment.objects.create(followup = followup,author = "Anonymous", comment_text =
                                        request.POST["body"], pub_date =
                                        timezone.now())
    return JsonResponse("", safe=False);
    #followup.followupComments.create(author = "Anonymous", comment_text =
#                                        request.POST["body"], pub_date =
 #                                       timezone.now())

