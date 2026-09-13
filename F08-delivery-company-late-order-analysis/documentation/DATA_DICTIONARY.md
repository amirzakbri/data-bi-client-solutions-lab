# Data Dictionary

| Table | Grain | Key | Purpose |
|---|---|---|---|
| hubs | One origin hub | hub_id | Hub and region reference |
| carriers | One carrier | carrier_id | Delivery partner reference |
| shipments | One shipment | shipment_id | Promise, outcome, service, lane, value, and reason |
| tracking_events | One shipment event | event_id | Created, dispatched, delivered, or failed scans |
| delivery_attempts | One attempt | attempt_id | First/repeat attempt results and failure reasons |

`on_time = delivered_at <= promised_at` for delivered shipments.  
`late_hours = max((delivered_at − promised_at) × 24, 0)`.  
`severe_late = late_hours > 24`.  
`first_attempt_success = successful first attempts / all first attempts`.
