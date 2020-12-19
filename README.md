My project is a web application that will help brazilian investors to have easy access to brazilian public companies data.

The main page of my application shows some market information. It has a tile showing IBOVESPA, that is the main brazilian stock market index. There is another tile showing IFIX, that is an index containing the main real estate funds in Brazil. Finally, the application has a tile for the oficial brazilian interest rate, a tile for the official brazilian inflation rate and a tile for a rate called CDI, that is normally used for brazilian fixed income bonds. Below these tiles, the application shows the latest news of the brazilian financial market.

The top of the web page has a link called “Ações” (that means “stocks” in english). This link opens a page where the user can see all the brazilian stocks. The left side of the page has a panel that the investor can use to filter the companies by sector and industry. Besides that, the investor can use a search field for find a particular company. This stock page has two view modes: Grid or list. The first one basically shows the company's logo and second one shows the logo, the sector name, the industry name and long description of company business.

When a user clicks on a company logo, the application opens the company’s page. This page shows three charts. The first one displays the income statement, the second displays the cash flow and the last one shows cash and long term debt.

The application was built with python, HTML, CSS, javascript and SQLLite. I have consumed Google's news API, RapidAPI for companies financial data and a Brazilian Government API for oficial inflation and oficial interest rate.
