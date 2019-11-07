from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Relationship, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        hook = 0

        for form in self.forms:
            if form.cleaned_data['tag_main']:
                hook += 1

        if hook > 1:
            raise ValidationError('Может быть только один основной тег!')
        elif hook < 1:
            raise ValidationError('Должен быть хотя бы один основной тег!')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
