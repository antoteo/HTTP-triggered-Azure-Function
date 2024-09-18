import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Get the 'name' parameter from the query string or request body
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = None
        if req_body and 'name' in req_body:
            name = req_body['name']

    if name:
        return func.HttpResponse(f"Hello, {name}!")
    else:
        return func.HttpResponse(
            "Please pass a name in the query string or in the request body.",
            status_code=400
        )
