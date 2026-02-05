import streamlit as st

from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

st.set_page_config(page_title="AI Ops Assistant", layout="centered")

st.title("🤖 AI Operations Assistant")
st.caption("Planner → Executor → Verifier | Powered by Groq")

task = st.text_input("Enter your task:", "Hey, get me some info on OpenClaw.")

if st.button("Run Assistant"):

    planner = PlannerAgent()
    executor = ExecutorAgent()
    verifier = VerifierAgent()

    with st.spinner("Planning..."):
        plan = planner.plan(task)

    st.subheader("🧠 Plan")
    st.json(plan)

    with st.spinner("Executing tools..."):
        raw = executor.execute(plan)

    with st.spinner("Verifying output..."):
        final = verifier.verify(raw)

    st.subheader("✅ Final Result")
    st.json(final)
