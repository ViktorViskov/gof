from editor import Editor
from care_taker import CareTaker


def client_code(editor: Editor, care_taker:CareTaker) -> None:
    editor.set_content("First version")
    print(f"Content: {editor.get_content()}")

    care_taker.save_state(editor)
    editor.set_content("Second version")
    print(f"Content: {editor.get_content()}")

    editor.restore_state(care_taker.get_state(0))
    print(f"Content: {editor.get_content()}")

editor = Editor()
care_taker = CareTaker()

client_code(editor, care_taker)