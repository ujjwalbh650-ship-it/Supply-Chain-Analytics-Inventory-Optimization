from pathlib import Path
import duckdb


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    db_path = (script_dir / ".." / ".." / "supply_chain_analytics.duckdb").resolve()

    con = duckdb.connect(str(db_path))

    con.execute("""
    CREATE OR REPLACE TABLE silver_sales_transactions_lite AS
    SELECT
        UPPER(TRIM(transaction_id)) AS transaction_id,

        COALESCE(
            TRY_CAST(transaction_ts AS TIMESTAMP),
            TRY_STRPTIME(transaction_ts, '%d/%m/%Y %H:%M')::TIMESTAMP
        ) AS transaction_ts,

        CAST(
            COALESCE(
                TRY_CAST(transaction_ts AS TIMESTAMP),
                TRY_STRPTIME(transaction_ts, '%d/%m/%Y %H:%M')::TIMESTAMP
            ) AS DATE
        ) AS transaction_date,

        channel,
        UPPER(TRIM(location_id)) AS location_id,
        UPPER(TRIM(sku)) AS sku,
        CAST(qty AS INTEGER) AS qty,
        CAST(unit_price AS DOUBLE) AS unit_price
    FROM bronze_sales_transactions_lite;
    """)

    con.close()

    print("🟩 Created silver_sales_transactions_lite")


if __name__ == "__main__":
    main()