import io
import struct
import random

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
        best_match_length = 0
        best_match_offset = 0
        
        # Search back for matches
        search_window = max(0, i - 4096), i
        for j in range(search_window[0], search_window[1]):
            match_length = 0
            while (i + match_length < len(input_data) and 
                   input_data[j + match_length] == input_data[i + match_length] and 
                   match_length < 15):
                match_length += 1
            
            # Update best match if found and longer than 2 bytes
            if match_length > best_match_length and match_length >= 3:
                best_match_length = match_length
                best_match_offset = i - j
        
        # Encode the match or literal
        if best_match_length > 0:
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
        # If only one byte left, treat as literal
        if i + 1 >= len(compressed_data):
            decompressed.append(compressed_data[i])
            break
        
        # Check if we're processing a 2-byte token or literal
        try:
            token = struct.unpack('>H', compressed_data[i:i+2])[0]
        except struct.error:
            decompressed.append(compressed_data[i])
            i += 1
            continue
        
        # Extract offset and length
        offset = token >> 4
        length = token & 0x0F
        
        # Handle literals and matched sequences
        if offset == 0 and length == 0:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
        else:
            # Handle matched sequence with more robust error checking
            if len(decompressed) < offset:
                # Fallback to literal
                decompressed.append(compressed_data[i])
                i += 1
                continue
            
            # Copy matched sequence
            start = len(decompressed) - offset
            for j in range(length):
                if start + j >= len(decompressed):
                    break
                byte = decompressed[start + j]
                decompressed.append(byte)
            
            i += 2
    
    return bytes(decompressed)