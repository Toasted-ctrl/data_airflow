import requests

def api_request(request_data: dict) -> dict:

    if request_data['url_ext']:
        request_url = f"{request_data['base_url']}{request_data['url_ext']}"
    elif not request_data['url_ext']:
        request_url = request_data['base_url']

    try:
        response = requests.get(
            url=request_url,
            params=request_data['params'])
        
    except Exception:
        return {
            "status_code": 999,
            "data": None,
            "item_id": request_data['source_id']
        }
    
    if request_data['content_type'] == 'json':
        return_data = response.json()

    elif request_data['content_type'] == 'text/html':
        return_data = str(response.text)

    else:
        return_data = None
    
    return {
        "status_code": response.status_code,
        "data": return_data,
        "item_id": request_data['source_id']
    }