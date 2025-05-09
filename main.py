import gradio as gr
import difflib

qa_data = {
    "What does the eligibility verification agent (EVA) do?":
        "EVA checks patient eligibility instantly to avoid errors.",
    "What does the claims processing agent (CAM) do?":
        "CAM automates and speeds up claims handling.",
    "How does the payment posting agent (PHIL) work?":
        "PHIL posts payments automatically to patient accounts.",
    "Tell me about Thoughtful AI's Agents.":
        "They’re AI tools like EVA, CAM, and PHIL that automate healthcare tasks.",
    "What are the benefits of using Thoughtful AI's agents?":
        "They save time, lower costs, and reduce mistakes."
}


def get_answer(user_input):
    questions = list(qa_data.keys())
    match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.5)
    if match:
        return qa_data[match[0]]
    else:
        return "I'm sorry, I don't have a answer for that now."

iface = gr.Interface(
    fn=get_answer,
    inputs=gr.Textbox(label="Ask me about Thoughtful AI"),
    outputs=gr.Textbox(label="Answer"),
    title="Thoughtful AI Support Assistant",
    description="I’m Mahmoud’s AI buddy — ask me what Thoughtful AI’s agents can do (I’ve got the scoop)!"

)

if __name__ == "__main__":
    iface.launch()
