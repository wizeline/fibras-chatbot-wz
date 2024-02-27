# Translate Cloud Function

This Cloud Function is part of the GCP_Webhooks suite and is responsible for translating text from one language to another using Google Cloud's Translation API. It is designed to work in conjunction with Dialogflow to provide translations for user inputs and system responses based on the context provided by the fulfillment tags.

## Functionality

The function takes a JSON payload from an HTTP request which contains the text to be translated and the target language code. It uses the `translate_text_per_tag` function from the `utils_translate` module to determine the appropriate translation based on the tag provided in the request. The tags 'user_text' and 'vertex_response' are used to specify the direction of translation.

- `user_text`: Translates the input text to Spanish (es).
- `vertex_response`: Translates the input text from Spanish to the target language if it is not Spanish.

The function then returns a JSON response containing the translated text.

## Deployment

To deploy this function to Google Cloud Functions, use the following command:
```
gcloud functions deploy translate \
       --gen2 \
       --set-env-vars GOOGLE_CLOUD_PROJECT_ID=ai-nativeframework \
       --project ai-nativeframework \
       --runtime python39 \
       --trigger-http \
       --entry-point process_request \
       --region us-east1
```
