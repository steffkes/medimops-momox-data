isbn = IO.read(:stdio, :all)

{:ok, %HTTPoison.Response{body: html}} =
  HTTPoison.get(
    "https://www.medimops.de/produkte-C0/",
    [],
    follow_redirect: true,
    params: [fcIsSearch: 1, searchparam: String.trim(isbn)]
  )

{:ok, document} = Floki.parse_document(html)

Floki.find(document, "div.mxjs-variant-selector")
|> Enum.each(fn {"div", attributes, _} ->
  attributes
  |> Enum.into(%{})
  |> Map.take(["data-price", "data-listprice", "data-stock", "data-condition"])
  |> Jason.encode!()
  |> IO.puts()

end)
