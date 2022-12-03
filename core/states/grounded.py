#
# Mars Rover Design Team
# grounded.py
#
# Created on November 29, 2022
# Updated on December 1, 2022
#

import core
from core.states import DroneState


class Grounded(DroneState):
    """
    This is the default state for the state machine. In this state the program does
    nothing explicit. Its singular purpose is to keep the python program running to
    receive and transmit rovecomm commands from base station that configure the
    next leg’s settings and confirm them.
    """

    def on_event(self, event) -> DroneState:
        """
        Defines all transitions between states based on events

        :param event:
        :return: DroneState
        """
        state: DroneState = None

        # Maybe add NEW_COORDS as event, as in state machine diagram:
        if event == core.AutonomyEvents.NEW_COORDS:
             state = core.states.Navigating()

        elif event == core.AutonomyEvents.START:
            state = core.states.Navigating()

        elif event == core.AutonomyEvents.ABORT:
            state = self

        else:
            self.logger.error(f'Unexpected event {event} for state {self}')
            state = self

        # Call exit() if we are not staying the same state
        if state != self:
            self.exit()

        # Return the state appropriate for the event
        return state

    async def run(self):
        """
        Defines regular drone operation when under this state
        """
        # Send no commands to drive board, the watchdog will trigger and stop the drone
        # from flying anyway The only way to get out of this is through the state
        # machine enable(), triggered by RoveComm

        """
        # The run function for Idle is empty - Grounded should try to land before the drone turns off
                
        # Should create landing functionality similar to the below
        if altitude > 0:
            # Reduce the power of whatever keeps the drone in the air until altitude is 0
            # Maybe look for obstacles that could impair landing and move elsewhere?
            # Maybe use accelerometer to see how quickly drone is falling, adjust accordingly to stay below max speed
            # Should have max falling speed to prevent damage to drone
        
        # If altitude <= 0, drone does nothing because it is not receiving commands, stay in Grounded

        return self
        """
