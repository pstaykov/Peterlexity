from ResearchAI.core.agent import ResearchAgent

def main():
    print("Research Assistant with Tool Calling")
    print("==================================================")

    agent = ResearchAgent()

    query = input("Enter your research query: ")

    detail_raw = input("How detailed should the summary be (1–10, 1 = very brief, 10 = very explicit)? ")
    try:
        detail_level = int(detail_raw)
    except ValueError:
        detail_level = 5  # default

    # clamp between 1 and 10
    detail_level = max(1, min(10, detail_level))

    response = agent.research(query, detail_level=detail_level)

    print("\n===== Final Response =====")
    print(response)

    # ===== SAVE RESULT =====
    with open("research.txt", "a", encoding="utf-8") as f:
        f.write("=== QUERY ===\n")
        f.write(query + "\n\n")
        f.write("=== DETAIL LEVEL ===\n")
        f.write(str(detail_level) + "\n\n")
        f.write("=== RESULT ===\n")
        f.write(response + "\n")
        f.write("\n" + "="*60 + "\n\n")

    print("\nResult saved to research.txt ✔")

if __name__ == "__main__":
    main()
