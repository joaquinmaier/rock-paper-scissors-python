import cv2
import mediapipe as mp
import src.ui as ui
import src.bm as bm
from src.rps_move import RPSMove, counter_moves, get_player_move

MP_HANDS = mp.solutions.hands
HANDS = MP_HANDS.Hands()
MP_DRAW = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)


def main() -> None:
    bm.start_bm_counter()

    while True:
        read_ok, image = cap.read()
        if not read_ok:
            print("Failed to read VideoCapture!")
            continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = HANDS.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                MP_DRAW.draw_landmarks(image, hand_landmarks, MP_HANDS.HAND_CONNECTIONS)

                player_move = get_player_move(hand_landmarks)

                if player_move == RPSMove.NONE:
                    print('You aren\'t playing :(')
                    continue
                
                bot_move = counter_moves[player_move]

                print(f'{ui.PLAYER_PLAY_COLOR}You played {player_move}')
                print(f'{ui.BOT_PLAY_COLOR}I play {bot_move}')
                print(f'{ui.NO_COLOR}')

        cv2.imshow("Camera Viewer", image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    bm.show_bm_message()

if __name__ == '__main__':
    main()
