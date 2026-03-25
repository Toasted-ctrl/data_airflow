import requests

def api_request_json(request_data: dict) -> dict:

    if request_data.url_ext != None:
        request_url = f"{request_data.base_url}{request_url.url_ext}"
    else:
        request_url = request_data.base_url

    try:
        response = requests.get(
            url=request_url,
            params=request_data.params)
        
    except Exception:
        return {
            "status_code": 999,
            "data": None,
            "item_id": request_data.item_id
        }
    
    return {
        "status_code": response.status_code,
        "data": response.json(),
        "item_id": request_data.item_id
    }