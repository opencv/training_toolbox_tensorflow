"""
 Copyright (c) 2021 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import abc

from ote.interfaces.dataset import IDataset
from ote.interfaces.parameters import BaseTaskParameters

class ITask(metaclass=abc.ABCMeta):
    """
    This is a common interface for objects representing a taraining extensions task
    """

    @abc.abstractclassmethod
    def train(self, train_dataset: IDataset, val_dataset: IDataset, parameters: BaseTaskParameters.BaseTrainingParameters=None):
        """
        This method launches training of a new model starting from currently loaded pre-trained weights.
        After training the internal model state is updated and can be retrieved using the get_model_bytes() method.

        :param training_dataset: Dataset containing the training data
        :param val_dataset: Dataset containing the validation data
        :param parameters: Training parameters
        """
        pass

    @abc.abstractclassmethod
    def test(self, dataset: IDataset, parameters: BaseTaskParameters.BaseEvaluationParameters) -> (list, dict):
        """
        This method launches inference of current version of model on the given dataset.

        :param dataset: Dataset containing the test data
        :param parameters: Analyze parameters
        :return: Analysis results: a list of task-specific inference artifacts corresponding to items of the dataset
        and a dict containing computed evaluation metrics.
        """
        pass

    @abc.abstractclassmethod
    def cancel(self):
        """
        Cancels the running training process
        """
        pass

    @abc.abstractclassmethod
    def get_training_progress(self) -> int:
        """
        Returns progress of the training process in range of 0 to 100
        """
        pass

    @abc.abstractclassmethod
    def compress(self, parameters: BaseTaskParameters.BaseCompressParameters):
        """
        Performs model compression
        """
        pass

    @abc.abstractclassmethod
    def export(self, parameters: BaseTaskParameters.BaseExportParameters):
        """
        Performs export to OpenVINO
        """
        pass

    @abc.abstractclassmethod
    def load_model_from_bytes(self, binary_model: bytes):
        """
        Loads model from a binary representation
        """
        pass

    @abc.abstractclassmethod
    def get_model_bytes(self) -> bytes:
        """
        Returns the current model in binary format
        """
        pass
