def calcBlocks():
    full_width = int(input("Enter full width: "))
    block_width = int(input("Enter block width: "))
    percent = (block_width / full_width) * 100
    print(f"Block width is {percent:.2f}% of {full_width} width.")
