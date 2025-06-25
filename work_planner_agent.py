import streamlit as st
from smolagents import CodeAgent
from smolagents.models import InferenceClientModel
from smolagents.tools import tool
from huggingface_hub import login
import ssl
import certifi

# Fix SSL issues(if you get license verification issues. Can be excluded)
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())

# Hugging Face token login (replace with your token)
login("enter your hugging face token here")

# Define tool
@tool
def organize_work(task: str) -> str:
    """Organizes work tasks into structured steps.
    
    Args:
        task (str): A short description of the work task to plan.

    Returns:
        str: A step-by-step plan to execute the work task.
    """
    return f"""Planning for: "{task}"
1. Define the goal
2. Break into tasks
3. Estimate time
4. Assign priority
5. Schedule tasks
6. Set milestones and check-ins
"""

# Create agent
model = InferenceClientModel()
agent = CodeAgent(
    name="WorkPlanner",
    description="Plans and organizes work tasks",
    tools=[organize_work],
    model=model
)

# Streamlit UI
st.set_page_config(page_title="Work Planner Agent", page_icon="🗂️")

st.title("🗂️ Work Planner Agent")
st.write("Describe your work task below, and let the agent help you organize it!")

task_input = st.text_area("📝 Enter your work activity")

if st.button("Generate Plan") and task_input.strip():
    with st.spinner("Planning..."):
        result = agent.run(task_input)
    st.subheader("📋 Your Work Plan")
    st.code(result, language='markdown')
