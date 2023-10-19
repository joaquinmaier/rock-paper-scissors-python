
import cv2
import mediapipe as mp
from RPSMove import RPSMove
from MoveInterpreter import MoveInterpreter

cap = cv2.VideoCapture(0)
MP_HANDS = mp.solutions.hands
HANDS = MP_HANDS.Hands()
MP_DRAW = mp.solutions.drawing_utils

counter_moves: dict[RPSMove, RPSMove] = {
    RPSMove.ROCK:       RPSMove.PAPER,
    RPSMove.PAPER:      RPSMove.SCISSORS,
    RPSMove.SCISSORS:   RPSMove.ROCK
}

PLAYER_PLAY_COLOR = '\x1b[0;35m'
BOT_PLAY_COLOR = '\x1b[0;31m'
NO_COLOR = '\x1b[0m'


def get_player_move(hand_landmarks) -> RPSMove:
    landmarks = hand_landmarks.landmark

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
    

def main() -> None:
    while True:
        success, image = cap.read()
        if not success:
            print("Failed to read VideoCapture!")
            continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = HANDS.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, landmark in enumerate(hand_landmarks.landmark):
                    height, width, _ = image.shape
                    cx, cy = int(landmark.x * width), int(landmark.y * height)
                    if id == 8:
                        cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                        MP_DRAW.draw_landmarks(image, hand_landmarks, MP_HANDS.HAND_CONNECTIONS)

                        player_move = get_player_move(hand_landmarks)

                        if player_move == RPSMove.NONE:
                            print('You ain\'t playing :(')
                            continue
                        
                        bot_move = counter_moves[player_move]

                        print(f'{PLAYER_PLAY_COLOR}You played {player_move}')
                        print(f'{BOT_PLAY_COLOR}I play {bot_move}')
                        print(f'{NO_COLOR}')

        cv2.imshow("Camera", image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()