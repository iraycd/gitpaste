import datetime
from haystack.indexes import *
from haystack import site
from models import Note, Commit


class CommitIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    commit = CharField(model_attr='commit')
    user = CharField(model_attr='owner', null=True)

    def index_queryset(self):
        return Commit.objects.all()


class NoteIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    note = CharField(model_attr='note')
    filename = CharField(model_attr='filename')
    commit = CharField(model_attr='revision__commit')

    def index_queryset(self):
        return Note.objects.all()


site.register(Note, NoteIndex)
site.register(Commit, CommitIndex)
