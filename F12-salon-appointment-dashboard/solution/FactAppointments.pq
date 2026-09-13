let
    Source = Csv.Document(File.Contents(pAppointmentsPath),[Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers,{{"AppointmentID", type text},{"AppointmentDate", type date},{"AppointmentTime", type time},{"BookingDate", type date},{"CustomerID", type text},{"StaffID", type text},{"ServiceID", type text},{"Status", type text},{"BookingChannel", type text},{"DiscountPct", Percentage.Type},{"NetRevenue", Currency.Type},{"BookedMinutes", Int64.Type}}),
    ValidRows = Table.SelectRows(Types, each [AppointmentID] <> null and [AppointmentDate] <> null)
in ValidRows
