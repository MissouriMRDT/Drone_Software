#
# Mars Rover Design Team
# __init__.py
#
# Created on November 29, 2022
# Updated on December 1, 2022
#

from core.states.state import DroneState
from core.states.state_machine import StateMachine
from core.states.grounded import Grounded
from core.states.search_pattern import SearchPattern
from core.states.navigating import Navigating
from core.states.approaching_marker import ApproachingMarker
from core.states.approaching_gate import ApproachingGate
from enum import Enum

# State Machine handler, takes care of running states and enabling/disabling
# autonomy
state_machine: StateMachine


class AutonomyEvents(Enum):
    START = 1
    REACHED_GPS_COORDINATE = 2
    MARKER_SEEN = 3
    GATE_SEEN = 4
    MARKER_UNSEEN = 5
    SEARCH_FAILED = 6
    REACHED_MARKER = 7
    ALL_MARKERS_REACHED = 8
    ABORT = 9
    RESTART = 10
    # NO_WAYPOINT = 11
    NO_COORDS = 11
    # NEW_WAYPOINT = 12
    NEW_COORDS = 12


StateMapping = {
    'Grounded': 0,
    'Navigating': 1,
    'SearchPattern': 2,
    'ApproachingMarker': 3,
    'ApproachingGate': 4,
}
