users = {
    "Alice": ["Coding", "Music", "Hiking", "Pizza"],
    "Bob":   ["Movies", "Hiking", "Tacos"],
    "Charlie": ["Coding", "Pizza", "Gaming", "Music"],
    "David": ["Cooking", "Travel"]
}

user = "Alice"
target_interests = users[user]

best_match = None
max_shared = -1

for person, interests in users.items():
    if person == user:
        continue

    shared_count = 0

    for interest in interests:
        if interest in target_interests:
            shared_count += 1

    print(f"Comparing {user} with {person}... {shared_count} shared interests.")

    if shared_count > max_shared:
        max_shared = shared_count
        best_match = person

print("-" * 30)
print(f"Best match for {user} is {best_match} with {max_shared} shared interests.")
