import json


def get_cost_estimate(guest_count, venue_cost, catering_cost_per_guest, decor_cost, misc_coast):
    total_catering_cost = guest_count * catering_cost_per_guest
    total_cost = venue_cost + total_catering_cost + decor_cost + misc_coast
    return total_cost


def main():
    guest_count = int(input("Enter the number of guests: "))
    venue_cost = float(input("Enter the cost of the venue: "))
    catering_cost_per_guest = float(input("Enter the catering cost per guest: "))
    decor_cost = float(input("Enter the decoration cost: "))
    misc_cost = float(input("Enter the miscellaneous cost: "))

    total_cost = get_cost_estimate(guest_count, venue_cost, catering_cost_per_guest, decor_cost, misc_cost)
    print(f"The estimated total cost for the wedding is: ${total_cost:.2f}")

    # store result in json
    data = {
        'guest_count': guest_count,
        'venue_cost': venue_cost,
        'catering_cost_per_guest': catering_cost_per_guest,
        'decor_cost': decor_cost,
        'misc_cost': misc_cost,
        'total_cost': total_cost
    }
    with open('wedding_cost_estimate.json', 'w') as json_file:
        json.dump(data, json_file)

    print("Cost estimate saved to wedding_cost_estimate.json")


if __name__ == "__main__":
    main()
