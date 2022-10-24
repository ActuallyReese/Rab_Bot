
#############################################################################

def get_panda():
    response_data = {"fact": "Too many requests.", "image": "Please try again later."}
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animal/panda")
    api_response = json.loads(resp.text)
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        response_data["fact"] = api_response["fact"]
        response_data["image"] = api_response["image"]
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    return response_data

def get_dog():
    response_data = {"fact": "Too many requests.", "image": "Please try again later."}
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animal/dog")
    api_response = json.loads(resp.text)
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        response_data["fact"] = api_response["fact"]
        response_data["image"] = api_response["image"]
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    return response_data


def get_cat():
    response_data = {"fact": "Too many requests.", "image": "Please try again later."}
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animal/cat")
    api_response = json.loads(resp.text)
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        response_data["fact"] = api_response["fact"]
        response_data["image"] = api_response["image"]
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    return response_data

def get_fox():
    response_data = {"fact": "Too many requests.", "image": "Please try again later."}
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animal/fox")
    api_response = json.loads(resp.text)
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        response_data["fact"] = api_response["fact"]
        response_data["image"] = api_response["image"]
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    return response_data

def get_red_panda():
    response_data = {"fact": "Too many requests.", "image": "Please try again later."}
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animal/red_panda")
    api_response = json.loads(resp.text)
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        response_data["fact"] = api_response["fact"]
        response_data["image"] = api_response["image"]
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    return response_data

def get_koala():
    response_data = {"fact": "Too many requests.", "image": "Please try again later."}
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animal/koala")
    api_response = json.loads(resp.text)
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        response_data["fact"] = api_response["fact"]
        response_data["image"] = api_response["image"]
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    return response_data

def get_birb():
    response_data = {"fact": "Too many requests.", "image": "Please try again later."}
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animal/birb")
    api_response = json.loads(resp.text)
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        response_data["fact"] = api_response["fact"]
        response_data["image"] = api_response["image"]
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    return response_data

def get_raccoon():
    response_data = {"fact": "Too many requests.", "image": "Please try again later."}
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animal/raccoon")
    api_response = json.loads(resp.text)
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        response_data["fact"] = api_response["fact"]
        response_data["image"] = api_response["image"]
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    return response_data

def get_kangaroo():
    response_data = {"fact": "Too many requests.", "image": "Please try again later."}
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animal/kangaroo")
    api_response = json.loads(resp.text)
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        response_data["fact"] = api_response["fact"]
        response_data["image"] = api_response["image"]
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    return response_data


#############################################################################