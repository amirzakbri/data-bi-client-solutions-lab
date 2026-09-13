# Data model

| From | Cardinality | To | Filter |
|---|---:|---|---|
| FactAppointments[AppointmentDate] | Many-to-one | DimDate[Date] | Single |
| FactAppointments[CustomerID] | Many-to-one | DimCustomer[CustomerID] | Single |
| FactAppointments[StaffID] | Many-to-one | DimStaff[StaffID] | Single |
| FactAppointments[ServiceID] | Many-to-one | DimService[ServiceID] | Single |

Create `DimDate = CALENDAR(MIN(FactAppointments[AppointmentDate]), MAX(FactAppointments[AppointmentDate]))`, add Year, Month, Month Number, Weekday, and mark it as the date table. Sort Month by Month Number. Do not use bidirectional filtering.
