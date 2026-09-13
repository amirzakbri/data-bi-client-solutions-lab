let
 Source = Csv.Document(File.Contents(ParameterDataPath & "fact_sales.csv"),[Delimiter=",",Encoding=65001,QuoteStyle=QuoteStyle.Csv]),
 Headers = Table.PromoteHeaders(Source,[PromoteAllScalars=true]),
 Typed = Table.TransformColumnTypes(Headers,{{"SalesLineID",Int64.Type},{"DateKey",Int64.Type},{"ProductKey",Int64.Type},{"CustomerKey",Int64.Type},{"StoreKey",Int64.Type},{"Quantity",Int64.Type},{"DiscountPct",Percentage.Type},{"Revenue",Currency.Type},{"Cost",Currency.Type},{"GrossProfit",Currency.Type}}),
 Selected = Table.SelectColumns(Typed,{"SalesLineID","DateKey","ProductKey","CustomerKey","StoreKey","Quantity","DiscountPct","Revenue","Cost","GrossProfit"})
in Selected
