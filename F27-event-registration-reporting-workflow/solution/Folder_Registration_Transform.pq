let
    Source = Folder.Files(RegistrationFolder),
    VisibleCSV = Table.SelectRows(Source, each [Extension] = ".csv" and [Attributes]?[Hidden]? <> true),
    Parsed = Table.AddColumn(VisibleCSV, "Rows", each Table.PromoteHeaders(Csv.Document([Content],[Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]))),
    Combined = Table.Combine(Parsed[Rows]),
    CleanHeaders = Table.TransformColumnNames(Combined, each Text.Lower(Text.Replace(Text.Trim(_), " ", "_"))),
    Typed = Table.TransformColumnTypes(CleanHeaders,{
        {"registration_id", type text}, {"event_id", type text}, {"registration_date", type date},
        {"first_name", type text}, {"last_name", type text}, {"email", type text},
        {"company", type text}, {"ticket_type", type text}, {"source_channel", type text},
        {"registration_status", type text}, {"payment_status", type text},
        {"ticket_value", Currency.Type}, {"amount_paid", Currency.Type},
        {"attendance_status", type text}, {"consent_status", type text}
    }),
    StandardText = Table.TransformColumns(Typed,{
        {"email", each Text.Lower(Text.Trim(_)), type text},
        {"registration_status", each Text.Proper(Text.Trim(_)), type text},
        {"payment_status", each Text.Proper(Text.Trim(_)), type text},
        {"attendance_status", each Text.Proper(Text.Trim(_)), type text},
        {"consent_status", each Text.Proper(Text.Trim(_)), type text}
    })
in
    StandardText
