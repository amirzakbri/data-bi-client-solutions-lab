let
    Projects = Csv.Document(File.Contents(ParameterProjectsPath), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromotedProjects = Table.PromoteHeaders(Projects, [PromoteAllScalars=true]),
    TypedProjects = Table.TransformColumnTypes(PromotedProjects, {{"Project ID", type text}, {"Client ID", type text}, {"Start Date", type date}, {"End Date", type date}, {"Budget Hours", Int64.Type}, {"Contract Revenue", Currency.Type}, {"Budget Cost", Currency.Type}}),
    TimeSource = Csv.Document(File.Contents(ParameterTimeEntriesPath), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    TimeHeaders = Table.PromoteHeaders(TimeSource, [PromoteAllScalars=true]),
    TypedTime = Table.TransformColumnTypes(TimeHeaders, {{"Project ID", type text}, {"Hours", type number}, {"Labor Cost", Currency.Type}, {"Billable Hours", type number}}),
    TimeRollup = Table.Group(TypedTime, {"Project ID"}, {{"Actual Hours", each List.Sum([Hours]), type number}, {"Labor Cost", each List.Sum([Labor Cost]), Currency.Type}, {"Billable Hours", each List.Sum([Billable Hours]), type number}}),
    VendorSource = Csv.Document(File.Contents(ParameterVendorCostsPath), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    VendorHeaders = Table.PromoteHeaders(VendorSource, [PromoteAllScalars=true]),
    TypedVendor = Table.TransformColumnTypes(VendorHeaders, {{"Project ID", type text}, {"Amount", Currency.Type}}),
    VendorRollup = Table.Group(TypedVendor, {"Project ID"}, {{"Vendor Cost", each List.Sum([Amount]), Currency.Type}}),
    JoinTime = Table.NestedJoin(TypedProjects, {"Project ID"}, TimeRollup, {"Project ID"}, "Time", JoinKind.LeftOuter),
    ExpandTime = Table.ExpandTableColumn(JoinTime, "Time", {"Actual Hours", "Labor Cost", "Billable Hours"}),
    JoinVendor = Table.NestedJoin(ExpandTime, {"Project ID"}, VendorRollup, {"Project ID"}, "Vendor", JoinKind.LeftOuter),
    ExpandVendor = Table.ExpandTableColumn(JoinVendor, "Vendor", {"Vendor Cost"}),
    ActualCost = Table.AddColumn(ExpandVendor, "Actual Cost", each [Labor Cost] + [Vendor Cost], Currency.Type),
    GrossProfit = Table.AddColumn(ActualCost, "Gross Profit", each [Contract Revenue] - [Actual Cost], Currency.Type),
    GrossMargin = Table.AddColumn(GrossProfit, "Gross Margin", each [Gross Profit] / [Contract Revenue], Percentage.Type)
in
    GrossMargin

