from RPSMove import RPSMove
from HandLandmarks import HandLandmarks
import math
IMPORTANT_FINGERS_LIST: list[int] = [HandLandmarks.INDEX_FINGER_MCP, HandLandmarks.MIDDLE_FINGER_MCP, HandLandmarks.RING_FINGER_MCP, HandLandmarks.PINKY_MCP]

# ! Important note: the y axis is inverted in the hand landmarks. The top of the screen is 0, and the bottom is 1.

class MoveInterpreter():
    @staticmethod
    def is_rock(hand_landmarks) -> bool:
        # All tips must be lower than the MCPs
        print(f'{hand_landmarks.landmark[HandLandmarks.INDEX_FINGER_MCP].y} {hand_landmarks.landmark[HandLandmarks.INDEX_FINGER_TIP].y}')

        return all([hand_landmarks.landmark[landmark_code].y < hand_landmarks.landmark[landmark_code + 3].y for landmark_code in IMPORTANT_FINGERS_LIST]) and\
            abs(hand_landmarks.landmark[HandLandmarks.INDEX_FINGER_MCP].y - hand_landmarks.landmark[HandLandmarks.INDEX_FINGER_TIP].y) < 0.1
    @staticmethod
    def is_paper(hand_landmarks) -> bool:
        # All tips must be higher than the MCPs
        return hand_landmarks.landmark[HandLandmarks.INDEX_FINGER_MCP].y > hand_landmarks.landmark[HandLandmarks.INDEX_FINGER_TIP].y and\
            hand_landmarks.landmark[HandLandmarks.MIDDLE_FINGER_MCP].y > hand_landmarks.landmark[HandLandmarks.MIDDLE_FINGER_TIP].y and\
            hand_landmarks.landmark[HandLandmarks.RING_FINGER_MCP].y > hand_landmarks.landmark[HandLandmarks.RING_FINGER_TIP].y and\
            hand_landmarks.landmark[HandLandmarks.PINKY_MCP].y > hand_landmarks.landmark[HandLandmarks.PINKY_TIP].y

    @staticmethod
    def is_scissors(hand_landmarks) -> bool:
        # The tips of the index and middle fingers must be higher than the MCPs, and the tips of the ring and pinky fingers must be lower than the MCPs
        return hand_landmarks.landmark[HandLandmarks.INDEX_FINGER_MCP].y > hand_landmarks.landmark[HandLandmarks.INDEX_FINGER_TIP].y and\
            hand_landmarks.landmark[HandLandmarks.MIDDLE_FINGER_MCP].y > hand_landmarks.landmark[HandLandmarks.MIDDLE_FINGER_TIP].y and\
            hand_landmarks.landmark[HandLandmarks.RING_FINGER_MCP].y < hand_landmarks.landmark[HandLandmarks.RING_FINGER_TIP].y and\
            hand_landmarks.landmark[HandLandmarks.PINKY_MCP].y < hand_landmarks.landmark[HandLandmarks.PINKY_TIP].y
        
