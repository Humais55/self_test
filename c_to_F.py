tempe = float(input("Enter temperature to be converted: "))
choices = ["Fahrenheit to Celsius", "Celsius to Fahrenheit"]

print("\nChoose options: ")
for i, option in enumerate(choices, 1):
    print(f"{i}. {option}")

choice = int(input("\nSelect any option: "))

if choice == 1:
    C = (tempe - 32) / 1.8
    print(f"\n{tempe} degrees Fahrenheit is equal to {C:.2f} degrees Celsius.")
elif choice == 2:
    F = (tempe * 1.8) + 32
    print(f"\n{tempe} degrees Celsius is equal to {F:.2f} degree Fahrenheit")
else:
    print("\nSelect Valid Options!!")
