def show_result(title, value, unit="", interpretation=""):

    print("\n==========================")
    print(title)
    print("==========================")
    print(f"Result: {value} {unit}")

    if interpretation:
        print("\nInterpretation:")
        print(interpretation)

    print("==========================\n")