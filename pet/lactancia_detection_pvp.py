# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
To add a new task to PET, both a DataProcessor and a PVP for this task must
be added. The PVP is responsible for applying patterns to inputs and mapping
labels to their verbalizations (see the paper for more details on PVPs).
This file shows an example of a PVP for a new task.
"""

from typing import List

from pet.pvp import PVP, PVPS
from pet.utils import InputExample


class LactanciaTaskPVP(PVP):
    """
    Example for a pattern-verbalizer pair (PVP).
    """

    # Set this to the name of the task
    TASK_NAME = "lactancia-task"

    # Set this to the verbalizer for the given task: a mapping from the task's labels (which can be obtained using
    # the corresponding DataProcessor's get_labels method) to tokens from the language model's vocabulary
    VERBALIZER = {
        "1": ["Yes"],
        "2": ["No"]
    }

    def get_parts(self, example: InputExample):
        """
        This function defines the actual patterns: It takes as input an example and outputs the result of applying a
        pattern to it. To allow for multiple patterns, a pattern_id can be passed to the PVP's constructor. This
        method must implement the application of all patterns.
        """

        # We tell the tokenizer that both text_a and text_b can be truncated if the resulting sequence is longer than
        # our language model's max sequence length.
        text_a = self.shortenable(example.text_a)

        # For each pattern_id, we define the corresponding pattern and return a pair of text a and text b (where text b
        # can also be empty).
        if self.pattern_id == 0:
            return [text_a, 'Active wine producer?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'Active winery?', self.mask], []
        elif self.pattern_id == 2:
            return [text_a, 'Active vineyard?', self.mask], []
        elif self.pattern_id == 3:
            return [text_a, 'Active wine estate?', self.mask], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        return LactanciaTaskPVP.VERBALIZER[label]


# register the PVP for this task with its name
PVPS[LactanciaTaskPVP.TASK_NAME] = LactanciaTaskPVP
