// Type enforcement for Sales; create DimDate in DAX or import supplied calendar
+let
+ Source = Csv.Document(File.Contents(ParameterDataPath & "retail_sales.csv"),[Delimiter=",",Encoding=65001,QuoteStyle=QuoteStyle.Csv]),
+ Headers = Table.PromoteHeaders(Source,[PromoteAllScalars=true]),
+ Types = Table.TransformColumnTypes(Headers,{{"SaleID",type text},{"OrderDate",type date},{"ProductID",type text},{"Category",type text},{"Channel",type text},{"Region",type text},{"Quantity",Int64.Type},{"Revenue",Currency.Type},{"Cost",Currency.Type},{"Profit",Currency.Type}})
+in Types
+