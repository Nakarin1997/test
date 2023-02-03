"""
เขียนโปรแกรมอะไรก็ได้ที่อยาก present Python's skill set เจ๋ง ๆ ของตัวเอง
ข้อนี้ไม่ต้องทำก็ได้ ไม่มีผลลบกับการให้คะแนน แต่ถ้าทำมาเเล้วเจ๋งจริง ก็จะพิจารณาเป็นพิเศษ

"""
import random
from enum import IntEnum

class Action(IntEnum):
    ค้อน = 0
    กระดาษ = 1
    กรรไกร = 2
    

victories = {
    Action.กรรไกร: [Action.กระดาษ],
    Action.กระดาษ: [Action.ค้อน],
    Action.ค้อน: [Action.กรรไกร]
    
}

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"เลือกคำตอบของคุณ ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"ผู้เล่นทั้งสองฝ่ายเลือก {user_action.name}. เสมอกัน!")
    elif computer_action in defeats:
        print(f"{user_action.name} VS {computer_action.name}! คุณชนะ!")
    else:
        print(f"{computer_action.name} VS {user_action.name}! คุณแพ้.")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"คุณเลือกไม่ถูกต้อง. เลือกระหว่าง {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("เล่นอีกครั้ง? (y/n): ")
    if play_again.lower() != "y":
        break