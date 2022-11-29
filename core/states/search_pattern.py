#
# Mars Rover Design Team
# search_pattern.py
#
# Created on November 29, 2022
# Updated on November 29, 2022
#

import core
import algorithms
import interfaces
import asyncio
from core.states import DroneState


class SearchPattern(DroneState):
    """
    The searching state’s goal is to fly the drone in an ever expanding Archimedean spiral, searching for the AR Tag.
    The spiral type was chosen because of it’s fixed distance between each rotation’s path.
    """

    def start(self):
        """
        Schedule Search Pattern
        """

        pass

    def exit(self):
        """
        Cancel all state specific tasks
        """

        pass

    def on_event(self, event) -> DroneState:
        """
        Defines all transitions between states based on events

        :param event:
        :return: DroneState
        """

        state: DroneState = None

        if event == core.AutonomyEvents.MARKER_SEEN:
            state = core.states.ApproachingMarker()

        elif event == core.AutonomyEvents.GATE_SEEN:
            state = core.states.ApproachingGate()

        elif event == core.AutonomyEvents.START:
            state = self

        elif event == core.AutonomyEvents.SEARCH_FAILED:
            # Should try to land before entering Grounded, rover just entered Idle
            state = core.states.Grounded()

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
        Defines regular drone operation when under this state

        :return: DroneState
        """

        return self
