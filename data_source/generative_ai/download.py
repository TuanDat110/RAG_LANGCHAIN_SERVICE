import os
import wget

file_links = [
    {
        "title": "Attention Is All You Need",
        "url": "https://arxiv.org/pdf/1706.03762"
    },
    {
        "title": "BERT- Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "url": "https://arxiv.org/pdf/1810.04805"
    },
    {
        "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
        "url": "https://arxiv.org/pdf/2201.11903"
    },
    {
        "title": "Instruction Tuning for Large Language Models- A Survey",
        "url": "https://arxiv.org/pdf/2308.10792"
    },
    {
        "title": "Llama 2- Open Foundation and Fine-Tuned Chat Models",
        "url": "https://arxiv.org/pdf/2307.09288"
    },
    {
        "title": "DeepSeek LLM Scaling Open-Source Language Models with Longtermism",
        "url": "https://arxiv.org/pdf/2401.02954"
    },
    {
        "title": "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model",
        "url": "https://arxiv.org/pdf/2405.04434"
    },
    {
        "title": "DeepSeek-V3 Technical Report",
        "url": "https://arxiv.org/pdf/2412.19437"
    },
    {
        "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
        "url": "https://arxiv.org/pdf/2501.12948"
    },
    {
        "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
        "url": "https://arxiv.org/pdf/2210.03629"
    },
    {
        "title": "Retrieval-Augmented Generation (RAG)",
        "url": "https://arxiv.org/pdf/2005.11401"
    },
    

]

# def is_exist(file_link):
#     return os.path.exists(f"./{file_link['title']}.pdf")

# for file_link in file_links:
#     if not is_exist(file_link):
#         wget.download(file_link["url"], out=f"./{file_link['title']}.pdf")

# Hàm làm sạch tên file (tránh lỗi ký tự đặc biệt)
def sanitize_filename(title):
    return "".join(c for c in title if c.isalnum() or c in " ._-").strip()

def is_exist(filepath):
    return os.path.exists(filepath)

for file_link in file_links:
    # Làm sạch tên file
    title_clean = sanitize_filename(file_link["title"])
    filename = f"{title_clean}.pdf"
    filepath = os.path.join(".", filename)

    if not is_exist(filepath):
        print(f"\n📥 Downloading: {filename}")
        try:
            wget.download(file_link["url"], out=filepath)
            print(f"\n Saved: {filename}")
        except Exception as e:
            print(f"\n Failed to download {file_link['url']}: {e}")
    else:
        print(f" Already exists: {filename}")
