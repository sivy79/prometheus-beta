import io
import struct

def lzop_compress(input_data):
    """
    Implement a basic LZOP compression algorithm.
    
    Args:
        input_data (bytes): The input data to compress
    
    Returns:
        bytes: Compressed data in LZOP format
    
    Raises:
        ValueError: If input is not bytes
    """
    # Validate input
    if not isinstance(input_data, bytes):
        raise ValueError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not input_data:
        return b''
    
    # Simple LZ77-like compression with run-length encoding
    compressed = bytearray()
    i = 0
    while i < len(input_data):
        # Look for repeated sequences
        max_match_length = min(15, len(input_data) - i)
        best_match_length = 0
        best_match_offset = 0
        
        # Search back for matches
        for offset in range(1, min(4096, i + 1)):
            match_length = 0
            while (match_length < max_match_length and 
                   input_data[i - offset + match_length] == input_data[i + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = offset
        
        # Encode the match or literal
        if best_match_length >= 3:
            # Encode match (offset, length)
            token = (best_match_offset << 4) | (best_match_length & 0x0F)
            compressed.extend(struct.pack('>H', token))
            i += best_match_length
        else:
            # Encode literal
            compressed.append(input_data[i])
            i += 1
    
    return bytes(compressed)

def lzop_decompress(compressed_data):
    """
    Decompress data compressed with the custom LZOP algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        ValueError: If input is not bytes or cannot be decompressed
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise ValueError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not compressed_data:
        return b''
    
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Check if we can read a 2-byte token
        if i + 1 >= len(compressed_data):
            # If only one byte left, treat as literal
            decompressed.append(compressed_data[i])
            break
        
        # Read 2-byte token
        token = struct.unpack('>H', compressed_data[i:i+2])[0]
        
        # Extract offset and length
        offset = token >> 4
        length = token & 0x0F
        
        if offset == 0 and length == 0:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
        else:
            # Matched sequence
            if len(decompressed) < offset:
                raise ValueError("Invalid compressed data: offset exceeds decompressed buffer")
            
            # Copy matched sequence
            for j in range(length):
                byte = decompressed[-offset + j]
                decompressed.append(byte)
            
            i += 2
    
    return bytes(decompressed)