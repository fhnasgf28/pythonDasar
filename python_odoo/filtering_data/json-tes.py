import json

def compute_lot_id_domain(case="default"):
    """
    Simulasi fungsi _compute_lot_id_domain dengan berbagai case.
    """
    domain = [('id', '=', False)]  # default domain

    if case == "return":
        # Simulasi: lot dari origin_returned_move_id
        lot_ids = [101, 102, 103]
        domain = [('id', 'in', lot_ids)]

    elif case == "available_stock":
        # Simulasi: quants dengan stok tersedia
        lot_ids = [201, 202]
        domain = [('id', 'in', lot_ids)]

    elif case == "no_stock":
        # Simulasi: tidak ada stok
        domain = [('id', '=', False)]

    # Konversi ke JSON string
    return json.dumps(domain)

# --- Testing ---
print("Case default:", compute_lot_id_domain("default"))
print("Case return:", compute_lot_id_domain("return"))
print("Case available_stock:", compute_lot_id_domain("available_stock"))
print("Case no_stock:", compute_lot_id_domain("no_stock"))