def decompress_tile(group_a, group_b):
    decompressed_tile = ''
    for hex_a, hex_b in zip(group_a, group_b):
        bin_a = format(hex_a, '08b')
        bin_b = format(hex_b, '08b')
        for bit_a, bit_b in zip(bin_a, bin_b):
            decompressed_tile += ''.join(['0', '2', '1', '3'][2 * int(bit_a) + int(bit_b)])
    return decompressed_tile


def compress_tile(decompressed_tile):
    group_a = []
    group_b = []
    for i in range(0, len(decompressed_tile), 8):
        group_a_bits = ''
        group_b_bits = ''
        for j in range(8):
            if decompressed_tile[i+j] in ('1', '3'):
                group_a_bits += '1'
            else:
                group_a_bits += '0'
            if decompressed_tile[i+j] in ('2', '3'):
                group_b_bits += '1'
            else:
                group_b_bits += '0'

        # Ensure zero-padding for consistent 2-digit hex representation
        group_a.append(format(int(group_a_bits, 2), '02x'))
        group_b.append(format(int(group_b_bits, 2), '02x'))
    return group_a, group_b

# Testing the code
group_a = [0x33, 0x44, 0x55, 0x66]
group_b = [0x77, 0x88, 0x99, 0xAA]
decompressed_tile = decompress_tile(group_a, group_b)
print(decompressed_tile)
compressed_tile_a, compressed_tile_b = compress_tile(decompressed_tile)
print(f"group_a = {compressed_tile_a}")
print(f"group_b = {compressed_tile_b}")
