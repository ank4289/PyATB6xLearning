input_responce =int(input("Enter the responce \n"))

if input_responce == 404:
    print("❌ Failed API Request")
elif input_responce == 200:
    print("✅ Passed API Request")
else:
    print("Not valid responce")

