from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,FormView,CreateView

# Create your views here.

# class ReviewView(CreateView):
#     model=Review
#     form_class=ReviewForm
#     template_name="reviews/review.html"
#     success_url="/thankyou"

class ReviewView(FormView):
    form_class=ReviewForm
    template_name="reviews/review.html"
    success_url="/thankyou"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

# class ReviewView(View):
    
#     def get(self,request):
#         form =  ReviewForm()
        
#         return render(request,"reviews/review.html",{
#                 "form":form,
#             })
        
#     def post(self,request):
#         form = ReviewForm(request.POST)
        
#         if form.is_valid(): 
#             form.save()
#             return HttpResponseRedirect('/thankyou')
        
#         return render(request,"reviews/review.html",{
#                 "form":form,
#             })
        
# def  feedback(request):
#     reviews=Review.objects.all()
#     return render(request,"reviews/feedbacks.html",{
#         "feedbacks": reviews
#     })  
    
class FeedbacksView(ListView):
    template_name="reviews/feedbacks.html"
    model=Review
    context_object_name="feedbacks"#by default it is objects_list
    
    # def get_queryset(self):
    #     base_query= super().get_queryset()
    #     data=base_query.filter(rating__gt=2)
    #     return data
    
    
    
    # reviews=Review.objects.all()
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["feedbacks"] = self.reviews
    #     return context
    
# class ReviewDetailView(TemplateView):
#     template_name="reviews/review_detail.html"
#     def get_context_data(self, **kwargs):
#         review=Review.objects.get(id=kwargs['id'])
#         context = super().get_context_data(**kwargs)
#         context["feedback"] = review
#         return context
    
class ReviewDetailView(DetailView):
    template_name="reviews/review_detail.html"
    model=Review
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review=self.object
        request=self.request
        favorite_id=request.session.get('favorite_review')
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context
    
    
    
    

# def review(request):
    
#     if request.method=='POST':
#         form = ReviewForm(request.POST)
        
#         if form.is_valid(): 
#             form.save()
#             # r1=Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating'])
#             # r1.save()
#             print(form.cleaned_data)
#             print(r1)
#             return HttpResponseRedirect('/thankyou')
#     else:
#         form =  ReviewForm()
        
#     return render(request,"reviews/review.html",{
#                 "form":form,
#             })

class ThankyouView(TemplateView):
    template_name="reviews/thankyou.html"
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["message"] = "You have submitted the feedback!"
         return context
     
class AddFavouriteView(View):
    def post(self,request):
        review_id=request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"]=review_id
        return HttpResponseRedirect("/review_detail/"+review_id)
     
        

