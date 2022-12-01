#
# Mars Rover Design Team
# navigating.py
#
# Created on November 29, 2022
# Updated on November 29, 2022
#

import core
import interfaces
import algorithms
from core.states import DroneState


class Navigating(DroneState):
    """
    The goal of this state is to navigate to the GPS coordinates provided by base
    station in succession, the last of which is the coordinate provided by the
    judges for that leg of the task. Coordinates before the last are simply the
    operators in base station’s best guess of the best path for the drone due to
    terrain identified on RED’s map.
    """

    def start(self):
        """
        Schedule Navigating
        """

        pass

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

        if event == core.AutonomyEvents.NO_WAYPOINT:
            # Should try to land before entering Grounded, rover just entered Idle
            state = core.states.Grounded()

        elif event == core.AutonomyEvents.REACHED_MARKER:
            # Should try to land before entering Grounded, rover just entered Idle
            state = core.states.Grounded()

        elif event == core.AutonomyEvents.REACHED_GPS_COORDINATE:
            state = core.states.SearchPattern()

        elif event == core.AutonomyEvents.NEW_WAYPOINT:
            state = self

        elif event == core.AutonomyEvents.START:
            state = self

        elif event == core.AutonomyEvents.ABORT:
            # Should try to land before entering Grounded, rover just entered Idle
            state = core.states.Grounded()

        else:
            self.logger.error(f'Unexpected event {event} for state {self}')
            state = core.states.Idle()

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
