from enum import Enum
from .move_interpreter import MoveInterpreter

class RPSMove(Enum):
    """
    Representation of all possible moves in Rock Paper Scissors.
    Note: RPS = Rock Paper Scissors.
    """
    ROCK        = 'rock'
    PAPER       = 'paper'
    SCISSORS    = 'scissors'
    NONE        = 'none'

    def __str__(self):
        return self.value.upper()


counter_moves: dict[RPSMove, RPSMove] = {
    RPSMove.ROCK:       RPSMove.PAPER,
    RPSMove.PAPER:      RPSMove.SCISSORS,
    RPSMove.SCISSORS:   RPSMove.ROCK
}


def get_player_move(hand_landmarks) -> RPSMove:
    # There are exactly 4 landmarks in each finger of the hand. As such, taking the base landmark of each finger
    # and adding 3 to it will give us the tip of the finger. We can then compare the y values of the base and tip
    # landmarks to determine if the finger is open or closed.
    if MoveInterpreter.is_rock(hand_landmarks):
        return RPSMove.ROCK
    
    elif MoveInterpreter.is_paper(hand_landmarks):
        return RPSMove.PAPER
    
    elif MoveInterpreter.is_scissors(hand_landmarks):
        return RPSMove.SCISSORS
    
    else:
        return RPSMove.NONE
