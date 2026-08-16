from pathlib import Path
import duckdb


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    db_path = (script_dir / ".." / ".." / "supply_chain_analytics.duckdb").resolve()

    con = duckdb.connect(str(db_path))

    con.execute("""
    CREATE OR REPLACE TABLE silver_product_master_lite AS
    SELECT
        UPPER(TRIM(sku)) AS sku,
        TRIM(product_name) AS product_name,
        TRIM(category) AS category,
        TRIM(brand) AS brand,
        unit_cost
    FROM bronze_product_master_lite;
    """)

    con.close()

    print("🟩 Created silver_product_master_lite")


if __name__ == "__main__":
    main()