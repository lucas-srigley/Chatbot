import gradio as gr
# import AI script file

# ------------------------------------------------- #
# Temporary function for chat interface
def TemporaryFunction(message, history):
    if len(history) % 2 == 0:
        return f"Yes, I do think that '{message}'"
    else:
        return "I don't think so"
# ------------------------------------------------- #

# Construction of the application
with gr.Blocks() as app:
    gr.Markdown("# Easy-Train Chatbot")
    gr.ChatInterface(TemporaryFunction, theme=gr.themes.Soft())

if __name__ == "__main__":
    app.launch()