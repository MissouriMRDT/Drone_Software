#
# Mars Rover Design Team
# state.py
#
# Created on November 29, 2022
# Updated on December 1, 2022
#

import logging


class DroneState:
    """
    A state class abstraction which serves as part of the state machine
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        # Call start(), use to schedule tasks
        self.start()

    async def run(self):
        """
        Defines regular drone operation when under this state

        :return: DroneState
        """

        pass

    def on_event(self, event):
        """
        Defines all transitions between states based on events

        :param event:
        :return: DroneState
        """

        pass

    def start(self):
        """
        Schedule State
        """

        pass

    def exit(self):
        """
        Cancel all state specific tasks
        """

        pass

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(self.__class__.__name__)

    def __ne__(self, other):
        return str(self) != str(other)
