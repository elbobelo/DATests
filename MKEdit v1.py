def decompress_tile(group_a, group_b):
  decompressed_tile = ''
  for hex_a, hex_b in zip(group_a, group_b):
    bin_a = format(hex_a, '08b')
    bin_b = format(hex_b, '08b')
    for bit_a, bit_b in zip(bin_a, bin_b):
      decompressed_tile += ''.join(['0', '2', '1', '3'][2 * int(bit_a) + int(bit_b)])
  return decompressed_tile

# Ask for the starting address
start_address = int(input("Enter the starting address (in hex): "), 16)

# Read the compressed tiles from the 6502 ROM file
with open('MK2.rom', 'rb') as f:
    f.seek(start_address)  # Seek to the starting address
    tiles = []
    for _ in range(8):  # Read 8 tiles
        compressed_tile = [
            [ord(f.read(1)) for _ in range(8)], # Read 8 bytes for group A
            [ord(f.read(1)) for _ in range(8)]  # Read 8 bytes for group B
        ]
        tiles.append(decompress_tile(compressed_tile[0], compressed_tile[1]))

# Print the decompressed tiles
for i, tile in enumerate(tiles):
    print(f"Tile {i + 1}:")
    print(tile)
    print()