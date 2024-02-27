# Identify Language Cloud Function

This Cloud Function is a component of the GCP_Webhooks suite, specifically designed to identify the language of a given text input. It leverages Google Cloud's Translation API to detect the language and is intended to be used in conjunction with Dialogflow to facilitate language-specific processing of user inputs.

## Functionality

The function accepts a JSON payload via an HTTP request, which includes the text whose language needs to be identified. It utilizes the `identify_language` function from the `utils_translate` module to detect the language of the provided text.

Upon receiving the text, the function logs the input and then proceeds to identify the language. Once the language is detected, it is logged for verification and a JSON response is returned containing the language code of the user input.

## Deployment

To deploy this function to Google Cloud Functions, the following command is used:
```
gcloud functions deploy identifyLanguage \
       --gen2 \
       --set-env-vars GOOGLE_CLOUD_PROJECT_ID=ai-nativeframework \
       --project ai-nativeframework \
       --runtime python39 \
       --trigger-http \
       --entry-point process_request \
       --region us-east1
```