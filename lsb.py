

def encode_aud_data(filename, secret):
    import wave

    song = wave.open(filename+".wav", mode='rb')

    nframes = song.getnframes()
    frames = song.readframes(nframes)
    frame_list = list(frames)
    frame_bytes = bytearray(frame_list)

    data = secret

    res = ''.join(format(i, '08b') for i in bytearray(data, encoding='utf-8'))
    print("\nThe string after binary conversion :- " + (res))
    length = len(res)
    print("\nLength of binary after conversion :- ", length)

    data = data + '*^*^*'

    result = []
    for c in data:
        bits = bin(ord(c))[2:].zfill(8)
        result.extend([int(b) for b in bits])

    j = 0
    for i in range(0, len(result), 1):
        res = bin(frame_bytes[j])[2:].zfill(8)
        if res[len(res) - 4] == result[i]:
            frame_bytes[j] = (frame_bytes[j] & 253)  # 253: 11111101
        else:
            frame_bytes[j] = (frame_bytes[j] & 253) | 2
            frame_bytes[j] = (frame_bytes[j] & 254) | result[i]
        j = j + 1

    frame_modified = bytes(frame_bytes)

    stegofile = filename+"new.wav"
    with wave.open(stegofile, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    print("\nEncoded the data successfully in the audio file.")
    song.close()




def decode_aud_data(filename):
    import wave

    song = wave.open(filename+".wav", mode='rb')

    nframes = song.getnframes()
    frames = song.readframes(nframes)
    frame_list = list(frames)
    frame_bytes = bytearray(frame_list)

    extracted = ""
    p = 0
    for i in range(len(frame_bytes)):
        if (p == 1):
            break
        res = bin(frame_bytes[i])[2:].zfill(8)
        if res[len(res) - 2] == 0:
            extracted += res[len(res) - 4]
        else:
            extracted += res[len(res) - 1]

        all_bytes = [extracted[i: i + 8] for i in range(0, len(extracted), 8)]
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "*^*^*":
                print("The Encoded data was :--", decoded_data[:-5])
                p = 1
                break