#
# Mars Rover Design Team
# approaching_marker.py
#
# Created on November 29, 2022
# Updated on December 3, 2022
#

import core
import core.constants
import interfaces
import algorithms
from core.states import DroneState


class ApproachingMarker(DroneState):
    """
    Within approaching marker, the drone explicitly follows the spotted marker
    until it reaches an acceptable distance from the drone, or loses sight of it.
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
        Asynchronous state machine loop

        :return: DroneState
        """

        """
        if altitude != desired_altitude:
            # Change the power of whatever keeps the drone in the air until altitude is correct
            # Maybe use accelerometer to see how quickly drone is changing speed, adjust accordingly to stay within reasonable speed
            
        else: # If at correct altitude
        # Most of the Rover code would likely work, may need to modify driving toward the marker
            if core.vision.ar_tag_detector.is_marker():
                # Unlike gate, does not need to check that marker is seen in 5 frames in a row

                # Grab the AR tags
                tags = ---
                gps_data = ---
                orig_goal, orig_start, leg_type = ---

                # Orient based on AR Tag
                distance = ---
                angle = ---

                left, right = algorithms.follow_marker.drive_to_marker(0.4*core.MAX_DRIVE_POWER, angle)
                # Unlike ApproachingGate, uses 0.4 drive power

                # Unlike ApproachingGate, movement is done by calling run multiple times
                # ApproachingGate identifies gate and then calls run once with movement done in while loops with sleep(0.01)
                if distance < 1.25:
                    interfaces.drive_board.stop()
                    # Do anything needed when marker is reached
                    return self.on_event(core.AutonomyEvents.REACHED_MARKER)
                    # Should switch to Grounded and land
                else: # If marker not reached yet
                    self.logger.info(f"Driving to target with speeds: ({left}, {right})")
                    interfaces.drive_board.send_drive(left, right)
                    # Unlike gate, only drives once per function call
            else: #if marker not seen
                self.num_detection_attempts += 1
                self.gate_detection_attempts = 0

                # If we have attempted to track an AR Tag unsuccesfully
                # MAX_DETECTION_ATTEMPTS times, we will return to search pattern
                if self.num_detection_attempts >= core.MAX_DETECTION_ATTEMPTS:
                    self.logger.info("Lost sign of marker, returning to Search Pattern")
                    return self.on_event(core.AutonomyEvents.MARKER_UNSEEN)

        return(self)
        # Unless lost sign of marker or marker reached, stay in ApproachingMarker
        """
