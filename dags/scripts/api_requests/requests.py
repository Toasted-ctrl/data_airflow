import requests

def api_get_request(request_data: dict) -> dict:

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
            "source_id": request_data['source_id']
        }
    
    if request_data['content_type'] == 'application/json':
        return_data = response.json()

    elif request_data['content_type'] == 'text/html':
        return_data = {}
        return_data['data'] = str(response.text)

    else:
        return_data = None
    
    return {
        "status_code": response.status_code,
        "data": return_data,
        "source_id": request_data['source_id']
    }

def api_post_request(data: dict, api_url: str, api_key: str, api_key_name: str):

    """Posts data to API."""
    payload = {}
    payload['entries'] = []
    payload['entries'].append(data)

    response = requests.post(
        url=api_url,
        headers={api_key_name: api_key},
        json=payload)

    return response.status_code