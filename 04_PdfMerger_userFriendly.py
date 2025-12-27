import streamlit as st
from PyPDF2 import PdfWriter
import io

# 1. App Title (Updated to your name)
st.title("📄 Deepak Pdf Merger")
st.subheader("Easily combine multiple PDF files into one.")

# 2. Upload Files
uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} files uploaded successfully!")
    
    # 3. Final file name input
    final_name = st.text_input("Enter the name for your merged PDF:", "Deepak_Merged_File")
    
    # 4. The Merge Logic
    if st.button("Merge PDFs"):
        merger = PdfWriter()
        
        for pdf in uploaded_files:
            merger.append(pdf)
        
        output_pdf = io.BytesIO()
        merger.write(output_pdf)
        merger.close()
        
        # 5. Download Button
        st.download_button(
            label="📥 Download Your Merged PDF",
            data=output_pdf.getvalue(),
            file_name=f"{final_name}.pdf",
            mime="application/pdf"
        )