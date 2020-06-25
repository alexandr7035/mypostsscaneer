import settings

# Reads the service key from file-
def get_service_key():

    with open(settings.service_key_file) as f:
        # Delete \n symbol in the end
        service_key = f.read()[:-1]
    
    f.close()

    return service_key

