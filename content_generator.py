import google.generativeai as genai
import streamlit as st
import fitz  # PyMuPDF for PDF export

# Set Google API Key
genai.configure(api_key="AIzaSyC7LfLs-cR9LAwvl2a0Jxg0WbyL_gqJDyo")

# Streamlit UI
st.title("🚀 AI-Powered Content Generator (Google Gemini)")

# User Inputs
content_type = st.selectbox("Select Content Type:", ["Blog", "LinkedIn Post", "Ad Copy", "Product Description"])
topic = st.text_input("Enter Your Topic:")
keywords = st.text_area("Enter SEO Keywords (comma separated):")
tone = st.selectbox("Select Tone:", ["Professional", "Casual", "Persuasive", "Storytelling"])

# Generate AI Suggestions for Headings
if st.button("Suggest Headings"):
    prompt = f"Generate 5 engaging headings for a {content_type} about {topic}."
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    st.write(response.text)

# Generate AI Content
if st.button("Generate Content"):
    refined_prompt = f"Write a {tone.lower()} {content_type} about {topic} with the following SEO keywords: {keywords}."
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(refined_prompt)
    content_output = response.text

    st.write(content_output)

    # PDF Export
    if st.button("Export as PDF"):
        pdf_filename = "generated_content.pdf"
        doc = fitz.open()
        page = doc.new_page()
        page.insert_text((50, 50), content_output)
        doc.save(pdf_filename)
        doc.close()
        st.success("PDF saved! Download it from your system.")
