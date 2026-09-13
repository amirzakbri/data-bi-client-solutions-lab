let
    Source = Csv.Document(File.Contents(Parameter_RentLedgerPath), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    TypedColumns = Table.TransformColumnTypes(PromotedHeaders, {
        {"invoice_id", type text}, {"month", type text}, {"property_id", type text},
        {"property_name", type text}, {"district", type text}, {"manager", type text},
        {"unit_id", type text}, {"tenant_id", type text}, {"tenant_name", type text},
        {"due_date", type date}, {"rent_billed", Currency.Type}, {"amount_paid", Currency.Type},
        {"balance", Currency.Type}, {"paid_date", type date}, {"payment_status", type text},
        {"days_late", Int64.Type}, {"aging_bucket", type text}
    }),
    CleanText = Table.TransformColumns(TypedColumns, {
        {"property_name", Text.Trim, type text}, {"tenant_name", Text.Trim, type text},
        {"payment_status", Text.Trim, type text}, {"aging_bucket", Text.Trim, type text}
    })
in
    CleanText
