
# Read ROM data from file
with open('MK2.rom', 'rb') as f:
    rom_data = f.read()

# Dictionary to store named addresses
named_addresses = {}

while True:
    address = input("Enter an address (hex): ")
    try:
        address = int(address, 16)
    except ValueError:
        print("Invalid address. Please enter a hexadecimal value.")
        continue

    if address < 0 or address >= len(rom_data):
        print("Address out of range. Please enter a valid address.")
        continue

    # Convert the byte to a hexadecimal string
    hex_value = rom_data[address].to_bytes(1).hex()
    print(f"The HEX value at address {hex(address)} is {hex_value}.")

    save = input("Do you want to save the address? (yes/no): ")
    if save.lower() == "yes":
        name = input("Enter a name for the address: ")
        named_addresses[name] = hex(address)
        print("Address saved.")

    for name, address in named_addresses.items():
        print(f"{name}: {address}")