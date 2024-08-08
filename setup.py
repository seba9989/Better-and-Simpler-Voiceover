import gradio as gr
from gradio import flagging

subs = [
    "Test",
    "Test2"
]

def load_subs_fn(test):
    # return open(test).read()
    return subs


with gr.Blocks() as root:
    load_subs = gr.Interface(
        fn=load_subs_fn,
        inputs=["file"],
        outputs=gr.TextArea(label="Załadowane Napisy"),
        submit_btn="Przeanalizuj napisy",
        allow_flagging="never"
    )



root.launch()
