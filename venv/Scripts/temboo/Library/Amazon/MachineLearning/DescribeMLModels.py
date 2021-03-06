# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeMLModels
# Returns a list of MLModels that match the search criteria in the request.
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

class DescribeMLModels(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeMLModels Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DescribeMLModels, self).__init__(temboo_session, '/Library/Amazon/MachineLearning/DescribeMLModels')


    def new_input_set(self):
        return DescribeMLModelsInputSet()

    def _make_result_set(self, result, path):
        return DescribeMLModelsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeMLModelsChoreographyExecution(session, exec_id, path)

class DescribeMLModelsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DescribeMLModels
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_EQ(self, value):
        """
        Set the value of the EQ input for this Choreo. ((optional, string) The equal to operator. The MLModel results will have FilterVariable values that exactly match the value specified with EQ.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('EQ', value)
    def set_FilterVariable(self, value):
        """
        Set the value of the FilterVariable input for this Choreo. ((optional, string) Use one of the following variables to filter a list of MLModel: CreatedAt, Status, Name, IAMUser, TrainingDataSourceId, RealtimeEndpointStatus, MLModelType, Algorithm, TrainingDataURI.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('FilterVariable', value)
    def set_GE(self, value):
        """
        Set the value of the GE input for this Choreo. ((optional, string) The greater than or equal to operator. The MLModel results will have FilterVariable values that are greater than or equal to the value specified with GE.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('GE', value)
    def set_GT(self, value):
        """
        Set the value of the GT input for this Choreo. ((optional, string) The greater than operator. The MLModel results will have FilterVariable values that are greater than the value specified with GT.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('GT', value)
    def set_LE(self, value):
        """
        Set the value of the LE input for this Choreo. ((optional, string) The less than or equal to operator. The MLModel results will have FilterVariable values that are less than or equal to the value specified with LE.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('LE', value)
    def set_LT(self, value):
        """
        Set the value of the LT input for this Choreo. ((optional, string) The less than operator. The MLModel results will have FilterVariable values that are less than the value specified with LT.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('LT', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The maximum number of MLModel to include in the result.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('Limit', value)
    def set_NE(self, value):
        """
        Set the value of the NE input for this Choreo. ((optional, string) The not equal to operator. The MLModel results will have FilterVariable values not equal to the value specified with NE.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('NE', value)
    def set_NextToken(self, value):
        """
        Set the value of the NextToken input for this Choreo. ((optional, string) The ID of the page in the paginated results.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('NextToken', value)
    def set_Prefix(self, value):
        """
        Set the value of the Prefix input for this Choreo. ((optional, string) A string that is found at the beginning of a variable, such as Name or Id.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('Prefix', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Determines the sequence of the resulting list of MLModel. Valid values are: asc, dsc.)
        """
        super(DescribeMLModelsInputSet, self)._set_input('SortOrder', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the S3 endpoint you wish to access. The default region is "us-east-1".)
        """
        super(DescribeMLModelsInputSet, self)._set_input('UserRegion', value)

class DescribeMLModelsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DescribeMLModels Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Amazon.)
        """
        return self._output.get('Response', None)

class DescribeMLModelsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DescribeMLModelsResultSet(response, path)
