# --- Part 1: Define a function for the profile & calculations ---
def generate_profile(age: int) -> str:
    """Determine the life stage based on the user's age."""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


def main():
    print("Welcome!")


# --- Part 2: Get user get info ---
user_name = input("Enter your full name: ")
birth_year_str= input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

# Gather hobbies
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
hobbies.append(hobby)


# --- Part 3: Process and generate the profile ---
life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "birth_year": birth_year,
    "current_age": current_age,
    "life_stage": life_stage,
    "hobbies": hobbies,
    "age_in_2050": 2050 - birth_year,
}


# --- Part 4: Display the Output ---
print("\nProfile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['current_age']}")
print(f"Life Stage: {user_profile['life_stage']}")
print(f"Age in 2050: {user_profile['age_in_2050']}")

if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for h in hobbies:
        print(f"- {h}")
        

# The other output option
# print("\nProfile Summary:")
# for key in ["name", "current_age", "life_stage", "age_in_2050"]:
#     print(f"{key.replace('_', ' ').title()}: {user_profile[key]}")
