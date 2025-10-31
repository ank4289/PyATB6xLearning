def validate_status_code(responce_code):
    if responce_code >0:
        if responce_code== 200:
            print("Successfull request")
        else:
            print("error is the request")
    else:
        print("Error in the responce code value")
validate_status_code(200)
validate_status_code(400)
validate_status_code(responce_code=200)
validate_status_code(int(input("Enter your status code")))
