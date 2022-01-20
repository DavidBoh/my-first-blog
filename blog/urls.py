from django.urls import path
from . import views as p


urlpatterns = [
        path('', p.post_list, name='post_list'),
        path('post/<int:pk>/', p.post_detail, name='post_detail'),
        path('post/new',p.post_new, name='post_new'),
        path('post/<int:pk>/edit/', p.post_edit, name='post_edit'),
        path('drafts/', p.post_draft_list, name="post_draft_list"),
        path('post/<pk>/publish/', p.post_publish, name='post_publish'),
        path('post/<pk>/remove', p.post_remove, name='post_remove'),
]        



