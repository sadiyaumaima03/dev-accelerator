accelerator 
**Goal:** Complete 30/40-day engineering preparation program. 

## Why dictionaries matter for AI apps
AI APIs (like OpenAI or Anthropic) and web services return data formatted as JSON, which maps directly to Python dictionaries. Using dictionaries allows programs to dynamically handle key-value pairs, nested structures, and missing fields without throwing unexpected runtime crashes.

## Refactoring & Error Handling (Day 4)
- **Functions:** Modularized code into `load_companies()`, `qualify()`, and `report()` to improve reusability and readability.
- **Error Handling:** Implemented targeted `try/except` blocks to prevent missing or invalid data types (e.g., string revenue values) from crashing the execution pipeline.