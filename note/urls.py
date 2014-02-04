from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('note.views',
    url(r'^live/$', 'live_note', name='live_note'),
    url(r'^(?P<pk>\d+)/$', RedirectView.as_view(url= '/note/%(pk)s/')),
    url(r'^(?P<pk>\d+)/(?P<private_key>[a-zA-Z0-9]+)?/?$', RedirectView.as_view(url= '/note/%(pk)s/%(private_key)s/')),
    url(r'^owner/$', RedirectView.as_view(url= '/owner/all/')),
    url(r'^owner/anonymous/', 'user_notes', name='anon_notes'),
    url(r'^owner/(?P<owner>.+)/', 'user_notes', name='user_notes'),
    url(r'^note/(?P<pk>\d+)/adopt/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'note_adopt', name='note_adopt'),
    url(r'^note/(?P<pk>\d+)/embed/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'note_embed', name='note_embed'),
    url(r'^note/(?P<pk>\d+)/edit/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'note_edit', name='note_edit'),
    url(r'^note/(?P<pk>\d+)/fork/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'note_fork', name='note_fork'),
    url(r'^note/(?P<pk>\d+)/favorite/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'note_favorite', name='note_favorite'),
    url(r'^note/(?P<pk>\d+)/delete/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'note_delete', name='note_delete'),
    url(r'^note/(?P<pk>\d+)/raw/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'note_raw', name='note_raw'),
    url(r'^commit/(?P<pk>.+)/adopt/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'commit_adopt', name='commit_adopt'),
    url(r'^commit/(?P<pk>.+)/download/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'commit_download', name='commit_download'),
    url(r'^note/(?P<pk>\d+)/(?P<private_key>[a-zA-Z0-9]+)?/?$', 'note_view', name='note_view'),
    url(r'^users/$', 'users', name='users'),
    url(r'^favorites/$', 'favorites', name='favorites'),
    url(r'^accounts/login/$', 'login', name='login'),
    url(r'^accounts/logout/$', 'logout', name='logout'),
    url(r'^accounts/register/$', 'register', name='register'),
    url(r'^accounts/preference/$', 'preference', name='preference'),
    url(r'^accounts/timezone/$', 'set_timezone', name='set_timezone'),
    url(r'^$', 'note', name='note'),
)
