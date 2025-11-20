from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import Post,Author,Tag,Comment
from django.views.generic import TemplateView,ListView,DetailView
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpg",
#         "author": "Prajjwal",
#         "date": date(2021, 7, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Prajjwal",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "author": "Maximilian",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }
# ]

def get_date(post):
    return post['date']

# def fp(request):
#     latest_posts=Post.objects.all().order_by("-date")[:3]
#     #sorted_posts=sorted(all_post,key=get_date)
#     #latest_posts=sorted_posts[-3:]
#     return render(request,"blog/index.html",{"posts": latest_posts})

class Fp(ListView):
    template_name="blog/index.html"
    model=Post
    ordering=["-date"]
    context_object_name='posts'
    
    def get_queryset(self):
        query_set= super().get_queryset()
        data=query_set[:3]
        return data
    

# def posts(request):
#     all_posts=Post.objects.all()
#     return render(request,"blog/all-posts.html",{"posts": all_posts})

class Posts(ListView):
    template_name="blog/all-posts.html"
    model=Post
    ordering=["-date"]
    context_object_name="posts"

# def post_detail(request,slug):
#     identified_post=get_object_or_404(Post,slug=slug)
#     #all_post=Post.objects.all()
#     #identified_post=next(post for post in all_post if post['slug']==slug)
#     return render(request,"blog/post-detail.html",{"post": identified_post,"post_tags":identified_post.tag.all()})

class PostDetail(View):
    
    def is_stored_post(self,request,post_id):
        stored_posts=request.session.get('read_later_posts_ids')
        if stored_posts is not None:
            is_saved_for_later= post_id in stored_posts
        else:
            is_saved_for_later=False
    
        return is_saved_for_later
 
    def get(self,request,slug):
        identified_post=get_object_or_404(Post,slug=slug)
        return render(request,"blog/post-detail.html",{
            "post": identified_post,
            "post_tags":identified_post.tag.all(),
            "comment_form":CommentForm(),
            "comments":identified_post.comments.all().order_by("-id"),
            "saved_for_later":self.is_stored_post(request,identified_post.id),
            })
    
    def post(self,request,slug):
        comment_form=CommentForm(request.POST)
        identified_post=get_object_or_404(Post,slug=slug)
        if comment_form.is_valid():
             comment=comment_form.save(commit=False)
             comment.post=identified_post
             comment.save()
             return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
             
        return render(request,"blog/post-detail.html",{
            "post": identified_post,
            "post_tags":identified_post.tag.all(),
            "comment_form":comment_form,
            "comments":identified_post.comments.all().order_by("-id"),
            "saved_for_later":self.is_stored_post(request,identified_post.id),
            })
        
    
# class PostDetail(DetailView):
#     template_name="blog/post-detail.html"
#     model=Post
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_tag"]=self.object.tag.all()
#         context["comment_form"]=CommentForm()
#         print(context)
#         return context
        
class ReadLaterView(View):
        
    def get(self,request):
        read_later_posts={}
        read_later_posts_ids=request.session.get('read_later_posts_ids')
        if read_later_posts_ids:
            read_later_posts=Post.objects.filter(id__in=read_later_posts_ids)
        return render(request,"blog/read-later.html",{"posts": read_later_posts})
    
    def post(self,request):
        post_id=int(request.POST["post_id"])
        post_list=request.session.get('read_later_posts_ids')
        
        if post_list is None:
            post_list=[]
            
        if post_id not in post_list:
            post_list.append(post_id)
        else:
            post_list.remove(post_id)
        request.session["read_later_posts_ids"]=post_list
            
        return HttpResponseRedirect("/")
    
