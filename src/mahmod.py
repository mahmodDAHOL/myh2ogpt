import os

from gradio_client import Client
import gradio as gr
from gradio_themes import SoftTheme, get_stategy_title
from gradio.themes.utils import colors, sizes, fonts
from mahmod_css import get_css

file_types = []
instruction_label = "Enter to Submit, Shift-Enter for more lines"

# client = Client("https://d55ae6dd33cbb12544.gradio.live")
# test_file1 = r"\\wsl.localhost\Ubuntu\tmp\New Text Document.txt"
# test_file_local, test_file_server = client.predict(test_file1, api_name='/upload_api')

# chunk = True
# chunk_size = 512
# langchain_mode = 'MyData'
# h2ogpt_key = ''
# res = client.predict(test_file_server,
#                         langchain_mode, chunk, chunk_size, True,
#                         None, None, None, None,
#                         h2ogpt_key,
#                         api_name='/add_file_api')

# api_name = '/submit_nochat_api'  # NOTE: like submit_nochat but stable API for string dict passing
# instruction = "What is Whisper?"
# kwargs = dict(langchain_mode=langchain_mode,
#                 langchain_action="Query",
#                 top_k_docs=4,
#                 document_subset='Relevant',
#                 document_choice="ALL",
#                 max_new_tokens=256,
#                 max_time=300,
#                 do_sample=False,
#                 stream_output=False,
#                 )
# res_dict, client = run_client_gen(client, instruction, None, kwargs)
theme_args = list()
theme_kwargs = {"primary_hue" : colors.indigo,
                "secondary_hue" : colors.brown_red,
                "neutral_hue" : colors.gray}


theme = SoftTheme(**theme_kwargs)
btn_css = "#bttn {margin-top: 30px;}"
css_code = btn_css + get_css({"h2ocolors": False})

title = "strategy&"
demo = gr.Blocks(theme=theme, css=css_code, title="strategy&", analytics_enabled=False)

with  demo:
    # if description is not None:
    description = ""
    gr.Markdown(f"""
        {get_stategy_title(title, description)}
        """)
    normal_block = gr.Row(visible=True, equal_height=False, elem_id="col_container")

    with normal_block:
        side_bar = gr.Column(elem_id="sidebar", scale=1, min_width=100, visible=True)
        with side_bar:
            with gr.Accordion("Upload", open=True, visible=True):
                    with gr.Column():
                        with gr.Row(equal_height=False):
                                file_upload_api = gr.File(show_label=False,
                                                        file_types=['.' + x for x in file_types],
                                                        # file_types=['*', '*.*'],  # for iPhone etc. needs to be unconstrained else doesn't work with extension-based restrictions
                                                        file_count="multiple",
                                                        scale=1,
                                                        min_width=0,
                                                        elem_id="warning", elem_classes="feedback",
                                                        )
                                file_upload_text = gr.Textbox(visible=False)
                                upload_api_btn = gr.UploadButton("Upload File Results", visible=False)



                                # then no need for add buttons, only single changeable db

        col_tabs = gr.Column(elem_id="col-tabs", scale=10)
        with col_tabs:
            col_chat = gr.Column(visible=True)
            with col_chat:
                with gr.Row():
                    with gr.Column(scale=50):
                        with gr.Row(elem_id="prompt-form-row"):
                            label_instruction = 'Ask anything'
                            instruction = gr.Textbox(
                                    lines=1,
                                    label=label_instruction,
                                    placeholder=instruction_label,
                                    info=None,
                                    elem_id='prompt-form',
                                    container=True,
                            )
                            # attach_button = gr.UploadButton(
                            #     elem_id="attach-button" ,
                            #     value="",
                            #     label="Upload File(s)",
                            #     size="sm",
                            #     min_width=24,
                            #     file_types=['.' + x for x in file_types],
                            #     file_count="multiple",
                            #     visible=True)

                    submit_buttons = gr.Row( equal_height=False, visible=True)

                    with submit_buttons:
                        mw1 = 50
                        mw2 = 50
                        with gr.Column(min_width=mw1):
                            submit = gr.Button(value='Submit', variant='primary', size='lg',
                                                    min_width=mw1, elem_id="bttn")
                        with gr.Column(min_width=mw2):
                            clear_chat_btn = gr.Button(value="Clear", size='lg', min_width=mw2, elem_id="bttn")


favicon_file = "strategy_logo.svg"
favicon_path = favicon_file

demo.launch(
    favicon_path=favicon_path
)