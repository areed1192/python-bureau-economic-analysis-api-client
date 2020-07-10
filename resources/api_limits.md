# API Calling Limits

The API has default calling limits as shown below. These limits are meant to protect BEA’s API and webserver
infrastructure from activity that may be detrimental to that infrastructure and/or unfairly impede other API users.

- 1000 API calls per minute, and/or
- 30 errors per minute, and/or
- 200 MB (raw data) per minute.

Any user that exceeds the above calling limits will receive an explanatory error message for each API call until
the per-minute cause has expired. The best way to avoid such errors is to design your application to call the API
within these limits, e.g., programmatically regulate the frequency/size of API calls.
