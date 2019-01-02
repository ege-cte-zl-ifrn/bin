"""
MIT License

Copyright (c) 2018 IFRN - Campus EaD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from django.utils.translation import gettext as _
from django.db.models import Model, CharField, TextField, NullBooleanField, FileField, DateTimeField, SmallIntegerField,\
    BooleanField
from django.db.models import ManyToManyField
from django.contrib.auth.models import AbstractUser
from python_brfied import to_choice
import ege_django_theme


class SpecialNeed(Model):
    VISION = _('Visão')
    AUDITION = _('Audição')
    OTHERS = _('Outras')
    CHOICES = to_choice(VISION, AUDITION, OTHERS)

    name = CharField(_('name'), max_length=250, blank=False, null=False)
    category = CharField(_('category'), max_length=250, choices=CHOICES, blank=False, null=False)

    class Meta:
        verbose_name = _('special need')
        verbose_name_plural = _('special needs')

    def __str__(self):
        return "%s (%s)" % (self.name, self.category)


class Profile(AbstractUser):
    username = CharField(_('username'), max_length=150, primary_key=True)

    is_active = BooleanField(_('is active'), default=True)
    is_staff = BooleanField(_('staff status'), default=False)
    is_superuser = BooleanField(_('superuser status'), default=False)

    is_personal_email_public = NullBooleanField(_('show to all'))

    biografy = TextField(_('biografy'), blank=True, null=True)
    is_biografy_public = TextField(_('show to all'), blank=True, null=True)

    valid_photo = FileField(_('valid photo'))
    pending_photo = FileField(_('pending photo'))
    solicitation_at = DateTimeField(_('solicitation_at'), blank=True, null=True)
    approved_at = DateTimeField(_('approved at'), blank=True, null=True)
    approved_by = CharField(_('approved by'), max_length=250, blank=True, null=True)

    font_size = SmallIntegerField(_('font size'), blank=True, null=True)
    theme_skin = CharField(_('theme skin'), choices=ege_django_theme.skins, max_length=250, blank=True, null=True)
    legends = NullBooleanField(_('legends'), blank=True, null=True)
    sign_language = NullBooleanField(_('sign language'), blank=True, null=True)
    screen_reader = NullBooleanField(_('screen reader'), blank=True, null=True)

    special_needs = ManyToManyField(SpecialNeed, verbose_name=_('special needs'))
    is_special_needs_public = NullBooleanField(_('show to all'))

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return "%s (%s)" % (self.username, self.is_active)
