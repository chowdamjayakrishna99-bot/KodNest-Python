marks=int(input())
attendance=int(input())
project_status=input()
if marks>=75 and attendance>=65:
    if project_status=='completed':
        print("passed")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")