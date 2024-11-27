
from django.contrib import admin
from django.urls import path, include

from petzo_app import views

urlpatterns = [
    path('',views.login),
    path('logout',views.logout),
    path('login_post',views.login_post),
    path('view_vethostpital',views.view_vethostpital),
    path('view_vethostpital_search',views.view_vethostpital_search),
    path('verifyhospital',views.verifyhospital),
    path('sendreply',views.sendreply),

    path('verifypetshop', views.verifypetshop),
    path('accpet_petshop/<id>', views.accpet_petshop),
    path('reject_petshop/<id>', views.reject_petshop),

    path('verifypetshop_search', views.verifypetshop_search),
    path('viewacceptedpetshop',views.viewacceptedpetshop),
    path('block_shop/<id>',views.block_shop),
    path('unblock_shop/<id>',views.unblock_shop),

    path('viewcomplaintandrating',views.viewcomplaintandrating),
    path('viewcomplaintandrating_post',views.viewcomplaintandrating_post),
    path('viewpetshoprating',views.viewpetshoprating),
    path('viewuser',views.viewuser),
    path('viewuser_search', views.viewuser_search),
    path('adminhome', views.adminhome),
    path('view_hospital', views.view_hospital),
    path('vethostpital_block/<id>', views.vethostpital_block),
    path('vethostpital_unblock/<id>', views.vethostpital_unblock),
    path('hs_accept/<id>', views.hs_accept),
    path('hs_reject/<id>', views.hs_reject),
    path('send_reply/<id>', views.send_reply),
    path('send_reply_post', views.send_reply_post),


    path('hospital_reg', views.hospital_reg),
    path('hs_home', views.hs_home),
    path('hospital_view_user', views.hospital_view_user),
    path('hsview_profile', views.hsview_profile),
    path('hsedit_profile', views.hsedit_profile),
    path('edit_profile_post', views.edit_profile_post),
    path('hs_view_rating', views.hs_view_rating),
    path('add_vaccine', views.add_vaccine),
    path('view_vaccines', views.view_vaccines),
    path('view_vaccines_post', views.view_vaccines_post),
    path('edit_vaccine_post', views.edit_vaccine_post),
    path('delete_vaccine/<id>', views.delete_vaccine),
    path('edit_vaccine/<id>', views.edit_vaccine),
    path('accept_vaccine_request/<id>', views.accept_vaccine_request),
    path('reject_vaccine_request/<id>', views.reject_vaccine_request),

    path('shop_register', views.shop_register),
    path('petshop_home', views.petshop_home),
    path('shopview_profile', views.shopview_profile),
    path('shopedit_profile', views.shopedit_profile),
    path('shopedit_profile_post', views.shopedit_profile_post),

    path('add_service', views.add_service),
    path('shop_view_service', views.shop_view_service),
    path('edit_service_post', views.edit_service_post),
    path('delete_service/<id>', views.delete_service),
    path('edit_service/<id>', views.edit_service),
    path('view_request/<id>', views.view_request),

    path('add_pet', views.add_pet),
    path('shop_view_pet', views.shop_view_pet),
    path('shop_view_user', views.shop_view_user),

    path('delete_pet/<id>', views.delete_pet),
    path('edit_pet/<id>', views.edit_pet),
    path('edit_pet_post', views.edit_pet_post),

    path('update_service_request_status/<id>', views.update_service_request_status),
    path('update_service_request_status_post', views.update_service_request_status_post),
    path('accept_sevice_request/<id>', views.accept_sevice_request),
    path('reject_sevice_request/<id>', views.reject_sevice_request),

    path('shop_view_request', views.shop_view_request),
    path('accept_request/<id>', views.accept_request),
    path('reject_request/<id>', views.reject_request),
    path('update_status/<id>', views.update_status),
    path('update_status_post', views.update_status_post),
    path('shop_view_vaccine_request/<id>', views.shop_view_vaccine_request),

    path('hospital_chat_to_user/<id>', views.hospital_chat_to_user),
    path('hs_chat_view', views.hs_chat_view),
    path('hs_chat_send/<msg>', views.hs_chat_send),

    path('shop_chat_to_user/<id>', views.shop_chat_to_user),
    path('chat_view', views.chat_view),
    path('chat_send/<msg>', views.chat_send),



    path('flutter_login', views.flutter_login),
    path('user_reg', views.user_reg),
    path('user_profile', views.user_profile),
    path('edit_profile', views.edit_profile),
    path('send_complaint', views.send_complaint),
    path('user_view_reply', views.user_view_reply),
    path('user_View_Pet', views.user_view_pets),
    path('user_view_vaccine', views.user_view_vaccine),
    path('user_view_hospital', views.user_view_hospital),
    path('send_hs_rating', views.send_hs_rating),

    path('user_view_shop', views.user_view_shop),
    path('sent_v_request', views.sent_v_request),
    path('user_view_vaccine_status', views.user_view_vaccine_status),
    path('user_send_petcare_request', views.user_send_petcare_request),
    path('user_view_petcare_request', views.user_view_petcare_request),
    path('add_post', views.add_post),
    path('user_view_post', views.user_view_post),
    path('user_send_comment', views.user_send_comment),
    path('user_view_comment', views.user_view_comment),
    path('user_view_services', views.user_view_services),

    path('user_send_service_request', views.user_send_service_request),
    path('user_view_service_request_status', views.user_view_service_request_status),


    path('user_viewchat', views.user_viewchat),
    path('User_sendchat', views.User_sendchat),

    path('user_add_pet', views.user_add_pet),
    path('user_view_user_pets', views.user_view_user_pets),

    path('user_viewchat_to_hs', views.user_viewchat_to_hs),
    path('hs_add_tips', views.hs_add_tips),
    path('hs_view_tips', views.hs_view_tips),
    path('user_view_tips', views.user_view_tips),
    path('delete_tips/<id>', views.delete_tips),

]
