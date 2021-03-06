# -*- coding: utf-8 -*-

###############################################################################
#
# AddTags
# Tags an artist with one or more user supplied tags. 
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddTags, self).__init__(temboo_session, '/Library/LastFm/Artist/AddTags')


    def new_input_set(self):
        return AddTagsInputSet()

    def _make_result_set(self, result, path):
        return AddTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddTagsChoreographyExecution(session, exec_id, path)

class AddTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        super(AddTagsInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((string) Your Last.fm API Secret.)
        """
        super(AddTagsInputSet, self)._set_input('APISecret', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((string) The artist name.)
        """
        super(AddTagsInputSet, self)._set_input('Artist', value)
    def set_SessionKey(self, value):
        """
        Set the value of the SessionKey input for this Choreo. ((string) The session key retrieved in the last step of the authorization process.)
        """
        super(AddTagsInputSet, self)._set_input('SessionKey', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((string) A comma delimited list of user supplied tags to apply to this artist. Accepts a maximum of 10 tags.)
        """
        super(AddTagsInputSet, self)._set_input('Tags', value)

class AddTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class AddTagsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddTagsResultSet(response, path)
