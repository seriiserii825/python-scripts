def calcBlocks():
    max_width = input("Enter max width: ")
    if max_width.isdigit():
        max_width = int(max_width)
    else:
        print("Invalid input. Please enter a number.")
        return
    blocks_width = []

    while True:
        block = input("Enter block width (or 'done' to finish): ")
        if block.lower() == 'done':
            break
        elif block.isdigit():
            blocks_width.append(int(block))
        else:
            print("Invalid input. Please enter a number or 'done'.")
            continue

    percentages = []
    # calculate perenctages for each block, but for the last got from the rest
    for i in range(len(blocks_width) - 1):
        percentage = (blocks_width[i] / max_width) * 100
        percentages.append(percentage)
    # last block
    last_block = max_width - sum(blocks_width[:-1])
    percentages.append((last_block / max_width) * 100)
    # print all percentages
    print("Percentages:")
    for i in range(len(percentages)):
        print(f"Block {i + 1}: {percentages[i]:.2f}%")
