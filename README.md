# llm-news-summarizer

---

News Summarizer that works with AWS s3 and lambda to run a selenium web scraper lambda function that pulls \
information off of new websites listed by google News RSS feeds. This is then transferred to an openai langgraph application \
that cleans the webscraped raw text, then summarizes the information as specified by user custom direction. \
This is then displayed on the react site. Else if asked, also runs as an mp3 file that can be played as audio.

## Steps:

1. I used Terraform to deploy resources to the cloud. To do so, first download terraform using homebrew if on mac
2. Deploy just the ecr repo first
3. Deploy docker image of `app_scraper/` repo to ecr repo
4. Deploy rest of infra (lambda function) to aws to then have our web scraper ready to go
5. Deploy react App to s3
