let
 Source = Csv.Document(File.Contents(ParameterDataPath & "retail_dashboard_source.csv"),[Delimiter=",",Encoding=65001,QuoteStyle=QuoteStyle.Csv]),
 Headers = Table.PromoteHeaders(Source,[PromoteAllScalars=true]),
 Types = Table.TransformColumnTypes(Headers,{{"OrderID",type text},{"OrderDate",type date},{"ProductID",type text},{"ProductName",type text},{"Category",type text},{"Region",type text},{"Channel",type text},{"CustomerSegment",type text},{"Quantity",Int64.Type},{"DiscountPct",Percentage.Type},{"Revenue",Currency.Type},{"Cost",Currency.Type},{"GrossProfit",Currency.Type},{"RevenueTarget",Currency.Type}}),
 AddYearMonth = Table.AddColumn(Types,"YearMonth",each Date.ToText([OrderDate],"yyyy-MM"),type text)
in AddYearMonth
