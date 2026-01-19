# and or

age = 16
has_subscription = False
with_parent = True

if age >= 18 and has_subscription:
    print("Watch any movie")
elif age >= 13 and (has_subscription or with_parent):
    print("Watch teen movies")
else:
    print("Access denied")