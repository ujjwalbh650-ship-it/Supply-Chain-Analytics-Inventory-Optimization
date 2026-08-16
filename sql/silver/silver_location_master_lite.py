from pathlib import Path
import duckdb


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    db_path = (script_dir / ".." / ".." / "supply_chain_analytics.duckdb").resolve()

    con = duckdb.connect(str(db_path))

    con.execute("""
    CREATE OR REPLACE TABLE silver_location_master_lite AS
    SELECT
        UPPER(TRIM(location_id)) AS location_id,
        TRIM(location_name) AS location_name,
        UPPER(TRIM(location_type)) AS location_type,
        TRIM(region) AS region
    FROM bronze_location_master_lite;
    """)

    con.close()

    print("🟩 Created silver_location_master_lite")


if __name__ == "__main__":
    main()