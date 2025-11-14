from googleapiclient.discovery import build
from ..core.config import GOOGLE_API_KEY, GOOGLE_CX



def web_search(query):
    """
    Searches Google and returns results
    
    Args:
        query (str): Search query
        
    Returns:
        list: List of dicts with {title, url, snippet}
    """
    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        
        result = service.cse().list(
            q=query,
            cx=GOOGLE_CX,
            num=5
        ).execute()
        
        search_results = []
        if 'items' in result:
            for item in result['items']:
                search_results.append({
                    'title': item.get('title', 'No title'),
                    'url': item.get('link', ''),
                    'snippet': item.get('snippet', 'No description')
                })
        
        return search_results
        
    except Exception as e:
        print(f"Search error: {e}")
        return []


def format_search_results(results):
    """Convert search results to string for the model"""
    if not results:
        return "No results found."
    
    formatted = "Search Results:\n\n"
    for i, result in enumerate(results, 1):
        formatted += f"{i}. {result['title']}\n"
        formatted += f"   URL: {result['url']}\n"
        formatted += f"   {result['snippet']}\n\n"
    
    return formatted