import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pathlib import Path
from src.base.llm_model import get_hf_llm
from src.rag.main import build_rag_chain

def test_rag_pipeline():
    print("🔍 Kiểm tra dữ liệu PDF đầu vào...")
    genai_docs = "../data_source/generative_ai"
    pdf_files = list(Path(genai_docs).glob("*.pdf"))
    if not pdf_files:
        print("❌ Không tìm thấy file PDF nào trong thư mục:", genai_docs)
        return
    print(f"✅ Tìm thấy {len(pdf_files)} file PDF.")

    print("🧠 Load mô hình LLM...")
    llm = get_hf_llm("meta-llama/Llama-3.2-1B-Instruct", temperature=0.7)
    print("✅ LLM đã được load.")

    print("📚 Tạo chuỗi RAG từ tài liệu PDF...")
    try:
        rag_chain, retriever = build_rag_chain(llm, data_dir=genai_docs, data_type="pdf")
        print("✅ RAG chain đã tạo thành công.")
    except Exception as e:
        print("❌ Lỗi khi tạo chain RAG:", e)
        return

    print("🔎 Kiểm tra truy vấn với retriever...")
    try:
        results = retriever.get_relevant_documents("What is RAG?")
        print(f"✅ Truy vấn retriever trả về {len(results)} tài liệu:")
        for i, doc in enumerate(results[:3]):
            print(f"--- Doc {i+1} ---")
            print(doc.page_content[:300])
            print()
    except Exception as e:
        print("⚠️ Không thể truy vấn retriever:", e)

    print("💬 Thử hỏi câu hỏi với RAG chain...")
    try:
        question = "What is RAG?"
        response = rag_chain.invoke(question)  # đảm bảo là chuỗi, không phải dict
        print("✅ Câu hỏi:", question)
        print("✅ Trả lời:", response)
    except Exception as e:
        print("❌ Lỗi khi gọi chain:", e)

if __name__ == "__main__":
    test_rag_pipeline()
