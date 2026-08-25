def show_result(calculation, result, unit=""):
    print("\n" + "=" * 50)
    print(f"{'RESULT':^50}")
    print("=" * 50)

    print(f"\nCalculation : {calculation}")

    if unit:
        print(f"Result      : {result} {unit}")
    else:
        print(f"Result      : {result}")

    print("\n" + "=" * 50)