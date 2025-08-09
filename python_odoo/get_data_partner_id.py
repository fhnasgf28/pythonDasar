import os
import sys
from xmlrpc import client as xmlrpc


def get_env_or_arg(name: str, index: int, default: str | None = None) -> str:
    """Helper to read value from env var first, then CLI arg, else default.

    Args:
        name: Environment variable name (e.g., ODOO_URL)
        index: CLI argument index (1-based after script name)
        default: Fallback value if neither env nor CLI provided
    """
    val = os.getenv(name)
    if val:
        return val
    if len(sys.argv) > index:
        return sys.argv[index]
    if default is not None:
        return default
    print(f"Missing required value for {name}. You can set env {name} or pass it as arg {index}.")
    sys.exit(1)


def connect_odoo(url: str, db: str, username: str, password: str):
    """Authenticate and return (uid, models) XML-RPC handles."""
    common = xmlrpc.ServerProxy(f"{url}/xmlrpc/2/common")
    uid = common.authenticate(db, username, password, {})
    if not uid:
        print("Authentication failed. Check DB/username/password.")
        sys.exit(1)
    models = xmlrpc.ServerProxy(f"{url}/xmlrpc/2/object")
    return uid, models


def fetch_partners_approved(url: str, db: str, username: str, password: str, limit: int = 100):
    """Fetch res.partner records where state == 'approved'."""
    uid, models = connect_odoo(url, db, username, password)

    domain = [["state", "=", "approved"]]
    fields = ["id", "name", "state", "email", "phone"]

    partners = models.execute_kw(
        db,
        uid,
        password,
        "res.partner",
        "search_read",
        [domain],
        {"fields": fields, "limit": limit},
    )
    return partners


def main():
    # Read config from env or CLI args
    # Usage (CLI): python get_data_partner_id.py <URL> <DB> <USERNAME> <PASSWORD> [LIMIT]
    url = get_env_or_arg("ODOO_URL", 1)
    db = get_env_or_arg("ODOO_DB", 2)
    username = get_env_or_arg("ODOO_USERNAME", 3)
    password = get_env_or_arg("ODOO_PASSWORD", 4)
    limit_str = os.getenv("ODOO_LIMIT") or (sys.argv[5] if len(sys.argv) > 5 else "100")
    try:
        limit = int(limit_str)
    except ValueError:
        print(f"Invalid LIMIT '{limit_str}', defaulting to 100")
        limit = 100

    partners = fetch_partners_approved(url, db, username, password, limit=limit)
    print(f"Found {len(partners)} partner(s) with state='approved'.")
    for p in partners:
        print({k: p.get(k) for k in ["id", "name", "state", "email", "phone"]})


if __name__ == "__main__":
    main()

