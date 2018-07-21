from django.conf.urls import url
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views


app_name = 'account'

urlpatterns = [
    # 登录与退出
    url(r'^login/$', auth_views.login, {"template_name": "account/login.html"}),
    url(r'^logout/$', auth_views.logout, {"template_name": "account/logout.html"}),
    url(r'^login/$', auth_views.login, name='user_login'),
    url(r'^logout/$', auth_views.logout, name='user_logout'),
    # 用户注册
    url(r'^register/$', views.register, name="user_register"),
    # 修改密码
    url(r'^password-change/$', auth_views.password_change, {"post_change_redirect": "/account/password-change-done/"}, name="password_change"),
    url(r'^password-change-done/$', auth_views.password_change_done, name="password_change_done"),
    # 重置密码
    url(r'^password-reset/$', auth_views.password_reset, {"template_name": "account/password_reset_form.html",
                                                          "email_template_name": "account/password_reset_email.html",
                                                          "subject_template_name": "account/password_reset_subject.txt",
                                                          "post_reset_redirect": "/account/password-reset-done"}, name="password_reset"),
    url('^password-reset-done/$', auth_views.password_reset_done, {"template_name": "account/password_reset_done.html"}, name="password_reset_done"),
    # 注意post_reset_redirect使用的是绝对路径以/开头
    url('^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, {"template_name": "account/password_reset_confirm.html",
                                                                                                              "post_reset_redirect": "/account/password-reset-complete"},
                                                                                                               name="password_reset_confirm"),
    url('^password-reset-complete/$', auth_views.password_reset_complete, {"template_name": "account/password_reset_complete.html"}, name="password_reset_complete"),
    # 个人信息
    url('^my-information/$', views.myself, name='my_information'),
    url('^edit-my-information/$', views.myself_edit, name='edit_my_information'),
    url('^my-image/$', views.my_image, name="my_image")
]