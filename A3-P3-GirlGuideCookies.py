#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #: Brayden Creese 
#Student Name: W0491583

def girlGuide():

    while True:
        try:
            numOfGuides = int(input("Enter the number of guides selling cookies: "))
            break
        except ValueError:
            print("Invalid Input! Please enter a valid number for 'number of guides'.")

    guides = []

    for i in range(numOfGuides):
        name = input(f"\nEnter the name of guide #{i + 1}: ")
        sales = int(input(f"Enter the number of boxes sold by {name}: "))
        guides.append({"name": name, "sales": sales})

    totalSales = sum(guide["sales"] for guide in guides)
    avgSales = totalSales / numOfGuides
    
    max_sales = max(guide["sales"] for guide in guides)
    for guide in guides:
        if guide["sales"] == max_sales:
            guide["prize"] = "- Trip to Girl Guide Jamboree in Aruba!"
        elif guide["sales"] > avgSales:
            guide["prize"] = "- Super Seller Badge"
        elif guide["sales"] > 0:
            guide["prize"] = "- Left over cookies"
        else:
            guide["prize"] = "-"
    
    print("\nThe average number of boxes sold by each guide was {:.1f}".format(avgSales))
    print("\nGuide\t\tPrizes Won:")
    print("=" * 40)
    for guide in guides:
        print(f"{guide['name']}\t\t{guide['prize']}")


girlGuide()
