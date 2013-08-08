# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 OpenStack Foundation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from abc import abstractmethod

from neutron.api import extensions
from neutron.api.v2 import base
from neutron.api.v2 import attributes as attr
from neutron.openstack.common import jsonutils
from neutron import wsgi

RESOURCE_NAME = 'group'
RESOURCE_PLURALS = {
    'groups': 'group',
}

RESOURCE_ATTRIBUTE_MAP = {
    RESOURCE_NAME + 's': {
        'id': {
            'allow_post': False,
            'allow_put': False,
            'validate': {'type:uuid': None},
            'is_visible': True,
            'primary_key': True,
        },
        'name': {
            'allow_post': True,
            'allow_put': True,
            'validate': {'type:string': None},
            'default': '',
            'is_visible': True,
        },
        'description': {
            'allow_post': True,
            'allow_put': True,
            'validate': {'type:string': None},
            'default': '', 'is_visible': True
        },
        'tenant_id': {
            'allow_post': True,
            'allow_put': False,
            'validate': {'type:string': None},
            'required_by_policy': True,
            'is_visible': True,
        },
        'instance_id': {
            'allow_post': True,
            'allow_put': False,
            'validate': {'type:string': None},
            'is_visible': True,
        }
}


class Topology(object):
    def __init__(self):
        pass

    def get_plugin_interface(self):
        return TopologyPluginInterface

    @classmethod
    def get_name(self):
        return "Neutron Topology API"

    @classmethod
    def get_alias(self):
        return "TOPOLOGY"

    @classmethod
    def get_description(self):
        return "Create networks using logical topology semantics"

    @classmethod
    def get_namespace(self):
        return "http://www.foundry.att.com/api/ext/pie/v1.0"

    @classmethod
    def get_updated(self):
        return "2013-08-06T16:06:00-08:00"

    @classmethod
    def get_resources(self):
        """Returns Extension Resources for the Topology API"""

        attr.PLURALS.update(RESOURCE_PLURALS)
        plugin = manager.NeutronManager.get_plugin()
        params = RESOURCE_ATTRIBUTE_MAP.get(RESOURCE_NAME + 's')
        controller = base.create_resource(
                                           RESOURCE_NAME + 's',
                                           RESOURCE_NAME,
                                           plugin,
                                           params,
                                         )
        ext = extensions.ResourceExtension(RESOURCE_NAME + 's', controller)
        return [ext]


