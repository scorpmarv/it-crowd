from django.conf.urls import url
from .views import (
    BackscratcherList,
    BackscratcherDetail,
    BackscratcherListView,
    BackscratcherDetailView
)

urlpatterns = [
    url(
        r'^backscratchers/$',
        BackscratcherList.as_view(),
        name='get_post_backscratchers'
    ),
    url(
        r'^backscratchers/(?P<pk>[0-9]+)/$',
        BackscratcherDetail.as_view(),
        name='get_delete_update_backscratchers'
    ),
    url(
        r'^list/$',
        BackscratcherListView.as_view(),
        name='backscratchers-list'
    ),
    url(
        r'^detail/(?P<pk>[-\w]+)/$',
        BackscratcherDetailView.as_view(),
        name='backscratchers-detail'
    ),
]
