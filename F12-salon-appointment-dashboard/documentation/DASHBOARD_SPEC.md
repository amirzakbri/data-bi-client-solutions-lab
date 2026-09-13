# Dashboard specification

## Page 1 — Executive overview (16:9)

Top row slicers: Date, Staff, Service Category, Booking Channel.

Hero cards: Net Revenue; Total Appointments; Completion Rate; Average Ticket; No-show Rate.

Visuals:
- Line chart: Net Revenue by Month, with Revenue MoM % in tooltip.
- Clustered bar: Net Revenue and Completed Appointments by Service Category.
- 100% stacked bar: Appointment count by Status and Booking Channel.
- Matrix: Staff, Completed Appointments, Net Revenue, Average Ticket, No-show Rate.

## Page 2 — Operations and demand

- Heatmap: Weekday × appointment hour, colored by Total Appointments.
- Bar chart: Total Appointments by Service Name.
- Funnel: Total → Completed → Cancelled → No-show (or replace with status bar if funnel semantics feel misleading).
- Detail table for follow-up: Appointment Date, Time, Customer, Staff, Service, Status, Channel.

## Interaction rules
- Global slicers affect all visuals on both pages.
- Staff matrix cross-filters service and monthly charts.
- Tooltips show count, revenue, completion rate, and average ticket.
- Currency uses USD with two decimals; rates use one decimal percentage.
