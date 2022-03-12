#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_pubsub_topic
description:
- A named resource to which messages are sent by publishers.
short_description: Creates a GCP Topic
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  name:
    description:
    - Name of the topic.
    required: true
    type: str
  kms_key_name:
    description:
    - The resource name of the Cloud KMS CryptoKey to be used to protect access to
      messages published on this topic. Your project's PubSub service account (`service-{{PROJECT_NUMBER}}@gcp-sa-pubsub.iam.gserviceaccount.com`)
      must have `roles/cloudkms.cryptoKeyEncrypterDecrypter` to use this feature.
    - The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*` .
    required: false
    type: str
  labels:
    description:
    - A set of key/value label pairs to assign to this Topic.
    required: false
    type: dict
  message_storage_policy:
    description:
    - Policy constraining the set of Google Cloud Platform regions where messages
      published to the topic may be stored. If not present, then no constraints are
      in effect.
    required: false
    type: dict
    suboptions:
      allowed_persistence_regions:
        description:
        - A list of IDs of GCP regions where messages that are published to the topic
          may be persisted in storage. Messages published by publishers running in
          non-allowed GCP regions (or running outside of GCP altogether) will be routed
          for storage in one of the allowed regions. An empty list means that no regions
          are allowed, and is not a valid configuration.
        elements: str
        required: true
        type: list
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
    elements: str
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics)'
- 'Managing Topics: U(https://cloud.google.com/pubsub/docs/admin#managing_topics)'
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a topic
  google.cloud.gcp_pubsub_topic:
    name: test-topic1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - Name of the topic.
  returned: success
  type: str
kmsKeyName:
  description:
  - The resource name of the Cloud KMS CryptoKey to be used to protect access to messages
    published on this topic. Your project's PubSub service account (`service-{{PROJECT_NUMBER}}@gcp-sa-pubsub.iam.gserviceaccount.com`)
    must have `roles/cloudkms.cryptoKeyEncrypterDecrypter` to use this feature.
  - The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*` .
  returned: success
  type: str
labels:
  description:
  - A set of key/value label pairs to assign to this Topic.
  returned: success
  type: dict
messageStoragePolicy:
  description:
  - Policy constraining the set of Google Cloud Platform regions where messages published
    to the topic may be stored. If not present, then no constraints are in effect.
  returned: success
  type: complex
  contains:
    allowedPersistenceRegions:
      description:
      - A list of IDs of GCP regions where messages that are published to the topic
        may be persisted in storage. Messages published by publishers running in non-allowed
        GCP regions (or running outside of GCP altogether) will be routed for storage
        in one of the allowed regions. An empty list means that no regions are allowed,
        and is not a valid configuration.
      returned: success
      type: list
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import (
    navigate_hash,
    GcpSession,
    GcpModule,
    GcpRequest,
    remove_nones_from_dict,
    replace_resource_dict,
)
import json
import re

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            kms_key_name=dict(type='str'),
            labels=dict(type='dict'),
            message_storage_policy=dict(type='dict', options=dict(allowed_persistence_regions=dict(required=True, type='list', elements='str'))),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/pubsub']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), fetch)
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, self_link(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'pubsub')
    return return_if_object(module, auth.put(link, resource_to_request(module)))


def update(module, link, fetch):
    auth = GcpSession(module, 'pubsub')
    params = {'updateMask': updateMask(resource_to_request(module), response_to_hash(module, fetch))}
    request = resource_to_request(module)
    del request['name']
    return return_if_object(module, auth.patch(link, request, params=params))


def updateMask(request, response):
    update_mask = []
    if request.get('labels') != response.get('labels'):
        update_mask.append('labels')
    if request.get('messageStoragePolicy') != response.get('messageStoragePolicy'):
        update_mask.append('messageStoragePolicy')
    return ','.join(update_mask)


def delete(module, link):
    auth = GcpSession(module, 'pubsub')
    return return_if_object(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'name': name_pattern(module.params.get('name'), module),
        u'kmsKeyName': module.params.get('kms_key_name'),
        u'labels': module.params.get('labels'),
        u'messageStoragePolicy': TopicMessagestoragepolicy(module.params.get('message_storage_policy', {}), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'pubsub')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://pubsub.googleapis.com/v1/projects/{project}/topics/{name}".format(**module.params)


def collection(module):
    return "https://pubsub.googleapis.com/v1/projects/{project}/topics".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'name': name_pattern(module.params.get('name'), module),
        u'kmsKeyName': module.params.get('kms_key_name'),
        u'labels': response.get(u'labels'),
        u'messageStoragePolicy': TopicMessagestoragepolicy(response.get(u'messageStoragePolicy', {}), module).from_response(),
    }


def name_pattern(name, module):
    if name is None:
        return

    regex = r"projects/.*/topics/.*"

    if not re.match(regex, name):
        name = "projects/{project}/topics/{name}".format(**module.params)

    return name


class TopicMessagestoragepolicy(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'allowedPersistenceRegions': self.request.get('allowed_persistence_regions')})

    def from_response(self):
        return remove_nones_from_dict({u'allowedPersistenceRegions': self.request.get(u'allowedPersistenceRegions')})


if __name__ == '__main__':
    main()