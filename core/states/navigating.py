#
# Mars Rover Design Team
# navigating.py
#
# Created on November 29, 2022
# Updated on December 1, 2022
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

        if event == core.AutonomyEvents.NO_COORDS:
            # Should try to land before entering Grounded, rover just entered Idle
            state = core.states.Grounded()

        elif event == core.AutonomyEvents.REACHED_MARKER:
            # Should try to land before entering Grounded, rover just entered Idle
            state = core.states.Grounded()

        elif event == core.AutonomyEvents.REACHED_GPS_COORDINATE:
            state = core.states.SearchPattern()

        # elif event == core.AutonomyEvents.NEW_WAYPOINT:
        #    state = self
        elif event == core.AutonomyEvents.NEW_COORDS:
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

        """
        # Grounded only goes to Navigating and only Grounded goes to Navigating, assume drone on ground at start of navigating
        gps_data = core.waypoint_handler.get_waypoint()

        # If the gps_data is none, there were no waypoint coordinates to be grabbed,
        # so log that and return
        if gps_data is None:
            return self.on_event(core.AutonomyEvents.NO_COORDS)
            # If no waypoint coordinates to grab, go to Grounded

        # Anything after the above statement is assumed to have gps data
        if altitude <= desired_altitude:
            # Change the power of whatever keeps the drone in the air until altitude is correct
            # Maybe use accelerometer to see how quickly drone is changing speed, adjust speed accordingly

        else: # If at correct altitude
            goal, start, leg_type = gps_data.data()
            current = interfaces.nav_board.location()

            # Rover has obstacle avoidance here, not necessary for drone

            if (algorithms.gps_navigate.get_approach_status() != core.ApproachState.APPROACHING):
                # If no longer approaching waypoint coordinates because they have been reached

                # Check for any other waypoints - if there is one, set it as the new waypoint and repeat
                if not core.waypoint_handler.is_empty():
                    # Goes back to Navigating
                    return self.on_event(core.AutonomyEvent.NEW_COORDS)
                else: # If no waypoint, go to next state
                    # Stop any horizontal movement, stay at same altitude
                    interfaces.drive_board.stop() # Make sure drone doesn't crash

                    # Set goal and start to current location to reset (?)
                    core.waypoint_handler.set_goal(interfaces.nav_board.location())
                    core.waypoint_handler.set_start(interfaces.nav_board.location())

                    if leg_type == "POSITION": # If was navigating towards a location marker
                        # Activate light or anything else needed when gate completed
                        return self.on_event(core.AutonomyEvents.REACHED_MARKER)
                        # Currently state machine goes to Grounded, may not need to land after getting to location marker
                    else: # If navigating towards marker/gate coordinates
                        return self.on_event(core.AutonomyEvent.REACHED_GPS_COORDINATE)
                        # If coordinate of marker/gate is reached, enter Search Pattern

            left, right = algorithms.gps_navigate.calculate_move()
            interfaces.drive_board.send_drive(left, right)
            # If still approaching destination, continue moving at max speed

        return self
        """