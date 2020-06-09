# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.volto.socialsettings.testing import (
    VOLTO_SOCIALSETTINGS_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.volto.socialsettings is properly installed."""

    layer = VOLTO_SOCIALSETTINGS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if collective.volto.socialsettings is installed."""
        self.assertTrue(
            self.installer.isProductInstalled(
                "collective.volto.socialsettings"
            )
        )

    def test_browserlayer(self):
        """Test that ICollectiveVoltoSocialsettingsLayer is registered."""
        from collective.volto.socialsettings.interfaces import (
            ICollectiveVoltoSocialsettingsLayer,
        )
        from plone.browserlayer import utils

        self.assertIn(
            ICollectiveVoltoSocialsettingsLayer, utils.registered_layers()
        )


class TestUninstall(unittest.TestCase):

    layer = VOLTO_SOCIALSETTINGS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["collective.volto.socialsettings"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.volto.socialsettings is cleanly uninstalled."""
        self.assertFalse(
            self.installer.isProductInstalled(
                "collective.volto.socialsettings"
            )
        )

    def test_browserlayer_removed(self):
        """Test that ICollectiveVoltoSocialsettingsLayer is removed."""
        from collective.volto.socialsettings.interfaces import (
            ICollectiveVoltoSocialsettingsLayer,
        )
        from plone.browserlayer import utils

        self.assertNotIn(
            ICollectiveVoltoSocialsettingsLayer, utils.registered_layers()
        )
