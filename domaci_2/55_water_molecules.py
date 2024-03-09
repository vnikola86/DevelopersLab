def max_water_molecules(hydrogen, oxygen):

    # Each water molecule needs 2 hydrogen and 1 oxygen molecules
    # The limiting factor is the availability of hydrogen molecules
    max_water = hydrogen // 2

    # Ensure that there are enough oxygen molecules
    max_water = min(max_water, oxygen)

    return max_water

hydrogen = int(input("Enter the number of hydrogen molecules (H): "))
oxygen = int(input("Enter the number of oxygen molecules (O): "))

result = max_water_molecules(hydrogen, oxygen)
print(f"The maximum number of water molecules (H2O) that can be formed is: {result}")
