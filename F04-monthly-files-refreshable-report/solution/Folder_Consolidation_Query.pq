let
    Source = Folder.Files(Excel.CurrentWorkbook(){[Name="SourceFolder"]}[Content]{0}[Column1]),
    CsvOnly = Table.SelectRows(Source, each Text.Lower([Extension]) = ".csv" and not Text.StartsWith([Name], "~$")),
    ParseFiles = Table.AddColumn(CsvOnly, "Rows", each Table.PromoteHeaders(Csv.Document([Content],[Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]), [PromoteAllScalars=true])),
    Combined = Table.Combine(ParseFiles[Rows]),
    Types = Table.TransformColumnTypes(Combined,{{"Order ID", type text}, {"Order Date", type date}, {"Product", type text}, {"Category", type text}, {"Channel", type text}, {"Region", type text}, {"Quantity", Int64.Type}, {"Unit Price", Currency.Type}, {"Discount", Percentage.Type}, {"Revenue", Currency.Type}, {"Cost", Currency.Type}, {"Profit", Currency.Type}}),
    AddMonth = Table.AddColumn(Types, "Month", each Date.ToText([Order Date], "yyyy-MM"), type text),
    RemoveBlankOrders = Table.SelectRows(AddMonth, each [Order ID] <> null and Text.Trim([Order ID]) <> "")
in
    RemoveBlankOrders
