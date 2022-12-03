#
# Mars Rover Design Team
# approaching_gate.py
#
# Created on November 29, 2022
# Updated on December 3, 2022
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
            # Maybe use accelerometer to see how quickly drone is changing speed, adjust speed accordingly

        else: # If at correct altitude
            # Most of the Rover code would likely work, may need to modify driving toward the gate
            if core.vision.ar_tag_detector.is_gate():

                # Grab the AR tags
                tags = ---
                gps_data = ---
                orig_goal, orig_start, leg_type = ---

                # If 2 tags of gate seen in at least 5 frames, assume it is a gate
                if len(tags) == 2 and self.gate_detection_attempts >= 5 and leg_type == "GATE":
                    # Somehow calculate distance and bearing - probably similar to Rover
                    # Then calculate second point to run through gate

                    # targetBeforeGate and targetPastGate are 3 meters behind and ahead gate, respectively (?)
                    # target is the coordinates in the middle of the gate (?)
                    points = [targetBeforeGate, target, targetPastGate]

                    for point in points:
                        # Should be similar to Rover, just change what gps_navigate.calculatemove does
                        while algorithms.gps_navigate.get_approachstatus(---) == core.ApproachState.Approaching
                                left, right = algorithms.gps_navigate.calculate_move()
                                interfaces.drive_board.send_drive(left, right)
                                time.sleep(0.01)
                                # Keeps moving closer and waiting until no longer approaching
                                # Should change drive_board to drone equivalent as needed

                # After moving to each point, the gate has been reached
                # Activate light or anything else needed when gate completed
                return self.on_event(core.AutonomyEvents.REACHED_MARKER)
                # Should switch to Grounded and land

            else: #if gate not seen
                self.num_detection_attempts += 1
                self.gate_detection_attempts = 0

                # If we have attempted to track an AR Tag unsuccesfully
                # MAX_DETECTION_ATTEMPTS times, we will return to search pattern
                if self.num_detection_attempts >= core.MAX_DETECTION_ATTEMPTS:
                    self.logger.info("Lost sign of gate, returning to Search Pattern")
                    return self.on_event(core.AutonomyEvents.MARKER_UNSEEN)

        return self
        # Unless lost sign of gate or gate passed through, stay in ApproachingGate
        """
