#
# Mars Rover Design Team
# approaching_gate.py
#
# Created on November 29, 2022
# Updated on November 29, 2022
#

import core
import core.constants
import interfaces
import algorithms
from core.states import DroneState
import time
import math


class ApproachingGate(DroneState):
    """
    Within approaching gate, 3 waypoints are calculated in front of, between, and through the viewed gate,
    allowing the drone to traverse through the gate fully.
    """

    def start(self):
        """
        Schedule AR Tag detection
        """

        self.num_detection_attempts = 0
        self.gate_detection_attempts = 0

    def exit(self):
        """
        Cancel all state specific coroutines
        """

        pass

    def on_event(self, event) -> DroneState:
        """
        Defines all transitions between states based on events

        :param event:
        :return: DroneState
        """

        state: DroneState = None

        if event == core.AutonomyEvents.REACHED_MARKER:
            # Should try to land before entering Grounded, rover just entered Idle
            state = core.states.Grounded()

        elif event == core.AutonomyEvents.START:
            state = self

        elif event == core.AutonomyEvents.MARKER_UNSEEN:
            state = core.states.SearchPattern()

        elif event == core.AutonomyEvents.ABORT:
            # Should try to land before entering Grounded, rover just entered Idle
            state = core.states.Grounded()

        else:
            self.logger.error(f"Unexpected event {event} for state {self}")
            # Should try to land before entering Grounded, rover just entered Idle
            state = core.states.Grounded()

        # Call exit() if we are not staying the same state
        if state != self:
            self.exit()

        # Return the state appropriate for the event
        return state

    async def run(self) -> DroneState:
        """
        Asynchronous state machine loop

        :return: DroneState
        """

        return self
