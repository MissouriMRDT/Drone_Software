#
# Mars Rover Design Team
# search_pattern.py
#
# Created on November 29, 2022
# Updated on December 1, 2022
#

import core
import algorithms
import interfaces
import asyncio
from core.states import DroneState


class SearchPattern(DroneState):
    """
    The searching state’s goal is to fly the drone in an ever expanding Archimedean
    spiral, searching for the AR Tag. The spiral type was chosen because of its
    fixed distance between each rotation’s path.
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
            # Considering entering Navigating instead of Grounded
            state = core.states.Grounded()

        elif event == core.AutonomyEvents.ABORT:
            # Should try to land before entering Grounded, rover just entered Idle
            state = core.states.Grounded()

        else:
            self.logger.error(f'Unexpected event {event} for state {self}')
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

        """
        if altitude != desired_altitude:
            # Change the power of whatever keeps the drone in the air until altitude is correct
            # Maybe use accelerometer to see how quickly drone is changing speed, adjust accordingly to stay within reasonable speed

        else: # If at correct altitude
            gps_data = core.waypoint_handler.get_waypoint()
            goal, start, leg_type = gps_data.data()
            current = interfaces.nav_board.location()

            # Check to see if gate or marker detected
            # If so, immediately stop all movement to ensure we don't lose sight of the AR tag(s) 
            if core.vision.ar_tag_detector.is_gate() and leg_type == "GATE":
                # Stop any horizontal movement, stay at same altitude
                interfaces.drive_board.stop() # Make sure drone doesn't crash
            
                # Sleep for a brief second
                await asyncio.sleep(0.1)

                return self.onevent(core.AutonomyEvents.GATE_SEEN)
                # Go to ApproachingGate

            elif core.vision.ar_tag_detector.is_marker() and leg_type == "MARKER":
                # Stop any horizontal movement, stay at same altitude
                interfaces.drive_board.stop() # Make sure drone doesn't crash
            
                # Sleep for a brief second
                await asyncio.sleep(0.1)

                return self.onevent(core.AutonomyEvents.MARKER_SEEN)
                # Go to ApproachingMarker

            if algorithms.gps_navigate.get_approach_status(goal, current, start) != core.ApproachState.APPROACHING:
                # If approach status changed, if no longer approaching due to proximity
                # If next point in search pattern has been reached
            
                # Stop any horizontal movement, stay at same altitude
                interfaces.drive_board.stop() # Make sure drone doesn't crash
                # Sleep for a brief second before moving to the next point, allows for AR Tag to be picked up if present
                await asyncio.sleep(0.1)

                goal = algorithms.marker_search.calculate_next_coordinate(start, goal)
                core.waypoint_handler.set_goal(goal)
                # Sets next goal in search pattern, regardless of which search pattern algorithm is used

            left, right = algorithms.gps_navigate.calculate_move(goal, current, start, core.MAX_DRIVE_POWER)
            interfaces.drive_board.send_drive(left, right)
            # Continue moving towards next point in search pattern

        return self
        # Stay in search pattern until search fails or gate/marker seen
        """
        
