# SQL Debugging Report

**Assessment:** Ready to share  
**Reporting window:** 2025-01-01 through 2026-07-31  
**Engine:** SQLite 3

The most material error was a grain mismatch between order lines and promotion rows. Joining both detail tables directly multiplied line values on multi-promotion orders and overstated completed revenue by **$71,033.94**. The repair aggregates each detail table to one row per order before joining.

The corrected result is **$843,743.19** across **1,268 completed orders**. Annual unique customers are **214**, compared with the invalid summed-monthly result of **449**.

## Validation
All seven controls pass: revenue independently reconciles, order counts are preserved, all customers survive the outer join, the distinct-customer denominator is bounded, July date logic reconciles, inflated revenue is detected, and all foreign keys resolve.

## Caveat
SQLite is used for portability. The debugging principles are engine-independent, but date functions and query-plan syntax should be adapted for PostgreSQL, SQL Server, BigQuery, or Snowflake.
