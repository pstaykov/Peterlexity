import json

from ..config import client, MODEL_NAME, MAX_TOKENS, MAX_ITERATIONS
from ..tools.search import web_search, format_search_results
from ..tools.web import fetch_webpage
from ..tools.storage import save_source
from ..utils import load_json



class ResearchAgent:
    def __init__(self):
        self.tools = load_json("tools.json")
        self.system_prompt = """You are a research assistant. Use the available tools to search the web, fetch detailed content, and save important sources.

CRITICAL RULES:
- Use ONLY bullet points with short phrases (but detailed enough to be informative)
- NO full sentences, NO conversational text, NO pleasantries
- Every bullet point must cite source: [Source: Title]
- Organize hierarchically: Main Topic → Subtopics → Key Details
- Save important sources using save_source tool
- Do NOT ask if user needs more information
- Do NOT write "Key point:" or "Subtopic:" labels

REQUIRED FORMAT:
Main Topic: [Topic Name]
  Subtopic: [Category]
    - Detailed point [Source: Title]
    - Another detail [Source: Title]
    - More specific information [Source: Title]
  Subtopic: [Another Category]
    - Detailed point [Source: Title]
    - Related information [Source: Title]

Main Topic: [Another Topic]
  Subtopic: [Category]
    - Detailed point [Source: Title]"""
        self.system_prompt_template = """You are a research assistant. Use the available tools to search the web, fetch detailed content, and save important sources.

CRITICAL RULES:
- Use ONLY bullet points with short phrases (but detailed enough to be informative)
- NO full sentences, NO conversational text, NO pleasantries
- Every bullet point must cite source: [Source: Title]
- Organize hierarchically: Main Topic → Subtopics → Key Details
- Save important sources using save_source tool
- Do NOT ask if user needs more information
- Do NOT write "Key point:" or "Subtopic:" labels

DETAIL LEVEL:
- DETAIL_LEVEL ranges from 1 (very brief) to 10 (very explicit and exhaustive)
- If DETAIL_LEVEL is 1–3: very compact bullets, only most important points
- If DETAIL_LEVEL is 4–7: normal level of detail
- If DETAIL_LEVEL is 8–10: very detailed, many subpoints and nuances
- Current DETAIL_LEVEL: {detail_level}

REQUIRED FORMAT:
Main Topic: [Topic Name]
  Subtopic: [Category]
    - Detailed point [Source: Title]
    - Another detail [Source: Title]
    - More specific information [Source: Title]
  Subtopic: [Another Category]
    - Detailed point [Source: Title]
    - Related information [Source: Title]

Main Topic: [Another Topic]
  Subtopic: [Category]
    - Detailed point [Source: Title]"""

    
    def execute_tool(self, tool_name, arguments):
        """Execute the requested tool function"""
        if tool_name == "web_search":
            results = web_search(arguments["query"])
            return format_search_results(results)
        
        elif tool_name == "fetch_webpage":
            return fetch_webpage(arguments["url"])
        
        elif tool_name == "save_source":
            return save_source(
                arguments["title"],
                arguments["url"],
                arguments["key_points"]
            )
        
        else:
            return f"Unknown tool: {tool_name}"
    
    def research(self, user_query, detail_level=5):
        """Main research function that uses tool calling"""
        # build system prompt dynamically based on detail level
        system_prompt = self.system_prompt_template.format(detail_level=detail_level)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
        
        iteration = 0
        
        while iteration < MAX_ITERATIONS:
            iteration += 1
            print(f"\n--- Iteration {iteration} ---")
            
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                tools=self.tools,
                max_tokens=MAX_TOKENS
            )
            
            assistant_message = response.choices[0].message
            
            if assistant_message.tool_calls:
                messages.append(assistant_message)
                
                for tool_call in assistant_message.tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    
                    print(f"Calling {function_name} with args: {function_args}")
                    
                    result = self.execute_tool(function_name, function_args)
                    
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": function_name,
                        "content": result
                    })
            
            else:
                final_answer = assistant_message.content
                print("\n" + "="*50)
                print("FINAL ANSWER:")
                print("="*50)
                print(final_answer)
                return final_answer
        
        return "Max iterations reached without final answer."