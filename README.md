# Peterlexity — lightweight research AI toolkit

Summary
- Peterlexity is a small research-oriented toolkit that orchestrates lightweight search and tool-based agents for experiments.
- Core runtime lives in the [ResearchAI](ResearchAI) package. See the entry point: [ResearchAI/main.py](ResearchAI/main.py) and config: [ResearchAI/config.py](ResearchAI/config.py).

Quick links
- Project root: [README.md](README.md)  
- Main script: [ResearchAI/main.py](ResearchAI/main.py)  
- Configuration and env: [ResearchAI/config.py](ResearchAI/config.py), [ResearchAI/.env](ResearchAI/.env)  
- Data manifests: [ResearchAI/sources.json](ResearchAI/sources.json), [ResearchAI/tools.json](ResearchAI/tools.json)  
- Core agent module: [`core.agent`](ResearchAI/core/agent.py) — see [ResearchAI/core/agent.py](ResearchAI/core/agent.py)  
- Tools package: [`tools.search`](ResearchAI/tools/search.py), [`tools.storage`](ResearchAI/tools/storage.py), [`tools.web`](ResearchAI/tools/web.py) — see [ResearchAI/tools](ResearchAI/tools)  
- Utilities: [`utils.file_loader`](ResearchAI/utils/file_loader.py) — see [ResearchAI/utils/file_loader.py](ResearchAI/utils/file_loader.py)

What it is and how it's made
- Purpose: provide a minimal architecture to combine a control Agent with modular Tools and simple file-based sources, enabling reproducible experiments and rapid prototyping.
- Architecture:
  - Agent (controller) — [ResearchAI/core/agent.py](ResearchAI/core/agent.py) coordinates tool calls and retrieval from sources.
  - Tools — modular helpers under [ResearchAI/tools](ResearchAI/tools): search, web, storage. Each tool exposes a clean interface and can be swapped or extended.
  - Sources & config — [ResearchAI/sources.json](ResearchAI/sources.json) defines data sources; [ResearchAI/tools.json](ResearchAI/tools.json) configures available tools; runtime config is in [ResearchAI/config.py](ResearchAI/config.py) and environment overrides live in [ResearchAI/.env](ResearchAI/.env).
  - Utilities — helpers like file loading in [ResearchAI/utils/file_loader.py](ResearchAI/utils/file_loader.py).

Installation
1. Requirements: Python 3.10+ recommended.
2. Create and activate a virtual environment:
   - Windows:
     - four backticks powershell
     - powershell
     - python -m venv .venv
     - .venv\Scripts\Activate.ps1
     - end
   - macOS / Linux:
     - four backticks bash
     - bash
     - python3 -m venv .venv
     - source .venv/bin/activate
     - end
3. Install dependencies:
   - If a requirements file exists, install it, e.g.:
     - pip install -r requirements.txt
   - Otherwise install commonly used libs used in research tooling (requests, beautifulsoup4, numpy, etc.) as needed.
4. Configure secrets and runtime flags:
   - Copy or edit [ResearchAI/.env](ResearchAI/.env) to add API keys and secrets used by tools.
   - Edit [ResearchAI/config.py](ResearchAI/config.py) for runtime toggles.

Usage
- Run the main experiment runner:
  - python ResearchAI/main.py
- To run specific modules for development, import the module and call its API:
  - Agent: import [`core.agent`](ResearchAI/core/agent.py) and instantiate its main class or entry function.
  - Tools: inspect [`ResearchAI/tools/search.py`](ResearchAI/tools/search.py), [`ResearchAI/tools/storage.py`](ResearchAI/tools/storage.py), and [`ResearchAI/tools/web.py`](ResearchAI/tools/web.py) for helper functions; wire them into the Agent.

Development notes
- Tests: none included — add unit tests under a tests/ folder and use pytest.
- Extending tools: implement the same interface shape as existing tools in [ResearchAI/tools](ResearchAI/tools) and add the tool entry to [ResearchAI/tools.json](ResearchAI/tools.json).
- Data sources: edit [ResearchAI/sources.json](ResearchAI/sources.json) to add or change data endpoints or local files.

Quick pointers to inspect code
- Entry point and orchestration: [ResearchAI/main.py](ResearchAI/main.py)  
- Agent logic: [`core.agent`](ResearchAI/core/agent.py) — open [ResearchAI/core/agent.py](ResearchAI/core/agent.py)  
- Tools: [ResearchAI/tools/search.py](ResearchAI/tools/search.py), [ResearchAI/tools/storage.py](ResearchAI/tools/storage.py), [ResearchAI/tools/web.py](ResearchAI/tools/web.py)  
- Utility loader: [ResearchAI/utils/file_loader.py](ResearchAI/utils/file_loader.py)  
- Manifests: [ResearchAI/sources.json](ResearchAI/sources.json), [ResearchAI/tools.json](ResearchAI/tools.json)

