import lsb

def main():
    encoded_file = lsb.encode("sound81.wav", "secret.txt")
    print(encoded_file)
    # decode_file = lsb.decode("secret.txt")
    # print(decode_file)







if __name__ == "__main__":
    main()