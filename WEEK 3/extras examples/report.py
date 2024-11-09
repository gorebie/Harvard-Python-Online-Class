def main():
    spacecraft = {"name": "Vogayer 1", "distance": 163}
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ======== REPORT ========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU
    
    ========================
    """

main()