import json
import os
from datetime import datetime


def save_source(title, url, key_points):
    """
    Save a source to sources.json
    
    Args:
        title (str): Title of the source
        url (str): URL of the source
        key_points (str): Key points or summary
        
    Returns:
        str: Confirmation message
    """
    try:
        source_entry = {
            "title": title,
            "url": url,
            "key_points": key_points,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        
        sources_file = "sources.json"
        
        if os.path.exists(sources_file):
            with open(sources_file, "r", encoding="utf-8") as f:
                try:
                    sources = json.load(f)
                    if not isinstance(sources, list):
                        sources = []
                except json.JSONDecodeError:
                    sources = []
        else:
            sources = []
        
        sources.append(source_entry)
        
        with open(sources_file, "w", encoding="utf-8") as f:
            json.dump(sources, f, indent=4, ensure_ascii=False)
        
        return f"Source '{title}' saved successfully."
    
    except Exception as e:
        return f"Error saving source: {str(e)}"


def get_saved_sources():
    """
    Retrieve all saved sources from sources.json
    
    Returns:
        list: List of saved sources
    """
    sources_file = "sources.json"
    
    try:
        if os.path.exists(sources_file):
            with open(sources_file, "r", encoding="utf-8") as f:
                sources = json.load(f)
                if not isinstance(sources, list):
                    return []
                return sources
        else:
            return []
    
    except Exception as e:
        print(f"Error retrieving saved sources: {str(e)}")
        return []