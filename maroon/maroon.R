library(tidyverse)
library(rvest)
library(httr)


maroon <- read_html("https://www.chicagomaroon.com/")

html_nodes(maroon, ".media-heading , .stronger-headline, .blurb-text, strong, .plain-link em", tr) %>% 
  html_text(df_raw, trim = T) %>% 
  View()