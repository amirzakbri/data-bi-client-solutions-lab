// Power Query pattern: enforce types before loading the fact table
let
 Source = Csv.Document(File.Contents(ParameterDataPath & "FactSales.csv"),[Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
 Headers = Table.PromoteHeaders(Source,[PromoteAllScalars=true]),
 Types = Table.TransformColumnTypes(Headers,{{"SalesLineKey",Int64.Type},{"OrderID",type text},{"DateKey",Int64.Type},{"CustomerKey",Int64.Type},{"ProductKey",Int64.Type},{"StoreKey",Int64.Type},{"Quantity",Int64.Type},{"DiscountPct",Percentage.Type},{"SalesAmount",Currency.Type},{"CostAmount",Currency.Type},{"ProfitAmount",Currency.Type}})
in Types
