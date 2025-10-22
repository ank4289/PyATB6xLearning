#count=1
#while count <5:
    #print(count)
    #count+=1

import random  # to simulate random API responses

attempt = 1

while attempt <= 3:
    # Simulate API response (either 200 or 500 randomly)
    response = int(input("Enter the responce"))
    print(f"Attempt {attempt}: Response {response}")

    if response == 200:
        print("✅ Test Passed")
        break  # exit loop if success
    attempt += 1

# if loop ends without success
if response != 200:
    print("❌ API failed after 3 attempts")
