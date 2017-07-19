from django.conf.urls import url
from . import views
from django.conf.urls import url
from blog import views as blog_views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^signup/$', blog_views.signup, name='signup'),
    url(r'^self-esteem/$', views.post_list_self_esteem, name='post_list_self-esteem'),
    url(r'^body-image/$', views.post_list_body_image, name='post_list_body-image'),
    url(r'^stress/$', views.post_list_stress, name='post_list_stress'),
    url(r'^bullying/$', views.post_list_bullying, name='post_list_bullying'),
    url(r'^depression/$', views.post_list_depression, name='post_list_depression'),
    url(r'^cyber-addiction/$', views.post_list_cyber_addiction, name='post_list_cyber-addiction'),
    url(r'^drinking-smoking/$', views.post_list_drinking_smoking, name='post_list_drinking-smoking'),
    url(r'^teen-pregnancy/$', views.post_list_teen_pregnancy, name='post_list_teen-pregnancy'),
    url(r'^underage-sex/$', views.post_list_underage_sex, name='post_list_underage-sex'),
    url(r'^child-abuse/$', views.post_list_child_abuse, name='post_list_child-abuse'),
    url(r'^peer-pressure/$', views.post_list_peer_pressure, name='post_list_peer-pressure'),
    url(r'^eating-disorders/$', views.post_list_eating_disorders, name='post_list_eating-disorders'),
    url(r'^LGBTQ/$', views.post_list_LGBTQ, name='post_list_LGBTQ'),
    url(r'^strict-parents/$', views.post_list_strict_parents, name='post_list_strict-parents'),
    url(r'^sleep/$', views.post_list_sleep, name='post_list_sleep'),
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
