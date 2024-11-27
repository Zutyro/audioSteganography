import lsb
import phase

def main():
    # lsb.encode_aud_data("watch-this-spoken_C_minor", "tohle je testova veta 2")
    # lsb.decode_aud_data("watch-this-spoken_C_minornew")
    # phase.encode("sound81.wav","Tohle je taky testova veta 3")
    print(phase.decode("encoded.wav"))




if __name__ == "__main__":
    main()