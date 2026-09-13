# Build and QA guide

1. Set each CSV privacy level consistently and disable automatic relationship discovery.
2. Apply data types before loading. AppointmentID must remain text.
3. Create one-to-many single-direction relationships from each dimension to the fact table.
4. Mark DimDate as the date table and sort month names numerically.
5. Paste measures individually from `measures.dax`.
6. Compare unfiltered cards with `validated_kpis.json`.
7. Test every slicer alone and in combination; clear selections before saving.
8. Confirm cancelled and no-show appointments produce zero revenue.
9. Save the downloadable semantic model as `F12_Salon_Appointment_Model.pbix` in `solution/`. If Power BI Service permits a full report download, additionally save it as `F12_Salon_Appointment_Dashboard.pbix`.
