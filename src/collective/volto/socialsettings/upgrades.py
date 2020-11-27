# -*- coding: utf-8 -*-
from collective.volto.socialsettings.interfaces import ISocialSettings
from plone import api

import logging
import json

logger = logging.getLogger(__name__)


DEFAULT_PROFILE = "profile-collective.volto.socialsettings:default"


def update_profile(context, profile):
    context.runImportStepFromProfile(DEFAULT_PROFILE, profile)


def update_registry(context):
    update_profile(context, "plone.app.registry")


def update_controlpanel(context):
    update_profile(context, "controlpanel")


def to_1001(context):
    """
    """
    update_registry(context)

