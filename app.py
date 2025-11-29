import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Authority Translator", page_icon="⚖️", layout="centered")

# --- HEADER ---
st.title("⚖️ The Authority Translator")
st.markdown("""
**Stop sounding defensive. Start sounding compliant.**
Turn your raw thoughts into diplomatic, authority-ready communication.
*Open Source by ADHOCON.*
""")
st.divider()

# --- INPUT SECTION ---
st.subheader("1. The Raw Draft (Your Honest Thoughts)")
raw_text = st.text_area(
    "Type what you REALLY want to say. Be emotional, be informal, use swear words if you have to. We will fix it.",
    height=150,
    placeholder="Example: Why are you asking for clinical data again? We already sent the CEP last month! This is ridiculous, the device is legacy! Read page 5!"
)

# --- SETTINGS ---
col1, col2 = st.columns(2)

with col1:
    target = st.selectbox(
        "2. Who is the recipient?",
        [
            "US FDA (Reviewer)",
            "EU Notified Body (Auditor)",
            "German Authority (BfArM/ZLG)",
            "Internal Management (C-Level)"
        ]
    )

with col2:
    tone = st.selectbox(
        "3. What is the Strategy?",
        [
            "Defensive (We are right, you are wrong - but polite)",
            "Apologetic (We messed up - here is the CAPA)",
            "Clarification (You missed information we already sent)",
            "Delaying (We need more time / Investigation ongoing)"
        ]
    )

# --- LOGIC ENGINE ---
def generate_transformation_prompt(target, tone, raw_input):
    
    # CONTEXT DEFINITIONS
    context_map = {
        "US FDA (Reviewer)": "concise, data-driven, unemotional. Cite 21 CFR 820 sections. Use terms like 'substantial equivalence' or 'least burdensome approach' if applicable.",
        "EU Notified Body (Auditor)": "cooperative, evidence-based. Reference ISO 13485:2016 and MDR Annexes. Emphasize 'State of the Art' and continuous improvement.",
        "German Authority (BfArM/ZLG)": "highly formal, bureaucratic German ('Behördendeutsch'). Use passive voice. Precise legal terminology. Reference specific paragraphs (§). Zero emotion.",
        "Internal Management (C-Level)": "executive summary style. Focus on: Risk of losing certificate, Timeline impact, and Cost. No technical jargon."
    }
    
    # TONE DEFINITIONS
    tone_map = {
        "Defensive": "Stand firm on our position but use 'interpretative consensus' language. Do not admit fault, but offer further explanation to align understanding.",
        "Apologetic": "Acknowledge the finding immediately. Move straight to the 'Correction' (immediate fix) and 'Corrective Action' (Systemic fix). Show control.",
        "Clarification": "Politely guide the reviewer to the specific page/document. Assume they simply missed it due to workload, do not imply they are incompetent.",
        "Delaying": "Express commitment to quality but justify the delay with 'thorough root cause investigation' or 'external validation dependencies'."
    }

    # THE MEGA PROMPT
    prompt = f"""
# SYSTEM ROLE
Act as a Senior Regulatory Affairs Expert and Crisis Communicator specializing in dealing with {target}.

# YOUR TASK
Rewrite the following DRAFT input into a formal, authority-ready response (Email or Official Letter).

# INPUT DRAFT (RAW)
"{raw_input}"

# TARGET AUDIENCE & STYLE
The recipient is: {target}.
The style must be: {context_map[target]}

# STRATEGIC INTENT
The strategy is: {tone}.
Execution instructions: {tone_map[tone]}

# RULES
1. Remove all emotion, aggression, sarcasm, or uncertainty.
2. Use standard regulatory terminology appropriate for the region.
3. If the draft implies data is missing, suggest a placeholder like [INSERT REFERENCE TO DOC X].
4. Output ONLY the rewritten text.
"""
    return prompt

# --- OUTPUT SECTION ---
if st.button("Generate Transformation Prompt"):
    if raw_text:
        final_prompt = generate_transformation_prompt(target, tone, raw_text)
        
        st.success("✅ Translation Logic Generated!")
        st.markdown("Copy the block below into **ChatGPT, Copilot, or Claude** to get your final letter.")
        st.code(final_prompt, language="markdown")
        
        st.info("💡 **Privacy Note:** We do not process your sensitive data here. This tool creates the *instruction* for your own secure AI.")
    else:
        st.error("Please enter your draft text first.")

# --- FOOTER ---
st.divider()
st.caption("Powered by ADHOCON Agentic Frameworks.")