def main():
    amount = 50
    
    while amount > 1:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))

        match coin:
            case 25 | 10 | 5:
                amount -= coin                    
            case _:
                print(f"Amoun Due: {amount}")
                
    print(f"Change Owed: {abs(amount)}")

main()