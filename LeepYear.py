print("Leep year Finder \n**************************")
dte = int(input("Enter any year to check is it Leep year or Not..."))
if dte % 4 == 0:
    print(f"{dte} is a Leep year.")
else:
    print(f"{dte} is not a Leep year.")