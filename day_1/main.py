def rotate():
    pass

def load_file(file_name: str) -> str:
    with open(file_name, "r") as f:
        return f.read()

def main():
    instr_data = load_file("input.txt")
    rotations = instr_data.split("\n")

    position = 50

    zero_lands = 0
    zero_passes = 0

    for rotation in rotations:
        position, zeros = rotate(position, rotation)

        if position == 0:
            zero_lands += 1
        
        zero_passes += zeros
    
    print(position)

if __name__ == "__main__":
    main()