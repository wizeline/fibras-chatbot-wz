# fibrasSitesWebhookService

The `fibrasSitesWebhookService` is a Google Cloud Function designed to handle webhook requests for site-related operations. It processes incoming requests, interacts with site management services to fetch or update site data, and formats the response according to the Dialogflow webhook response format.

## Functionality

- Logs incoming webhook requests for debugging and monitoring purposes.
- Converts the JSON request from Dialogflow into a format that can be processed by the site management services.
- Processes the request using the site management services to fetch relevant site information or perform site-related actions.
- Formats the response to be compatible with Dialogflow's expected webhook response structure.
- Logs the response before sending it back to Dialogflow.

## Deployment Instructions

Before deploying the `fibrasSitesWebhookService`, make sure you are located in the root folder of the function. Follow these steps to deploy using the Google Cloud CLI:

1. Ensure that you have the Google Cloud CLI (`gcloud`) installed and authenticated with your Google Cloud account.
2. Navigate to the root directory of the `fibrasSitesWebhookService` function.
3. Set the project ID with the following command:
   ```
   gcloud config set project ai-nativeframework
   ```
4. Deploy the function to Google Cloud Functions using the following command:
   ```
   gcloud functions deploy fibrasSitesWebhookServiceG2 \
       --gen2 \
       --project ai-nativeframework \
       --runtime python39 \
       --trigger-http \
       --entry-point dialogflow_request \
       --region us-east1
   ```
   This command sets the function name as `fibrasSitesWebhookServiceG2`, specifies the runtime environment as Python 3.9, triggers the function via HTTP requests,  sets the entry point to the `dialogflow_request` function, and specifies the region as `us-east1`.

5. Remember to set the necessary environment variables in the Google Cloud project settings to ensure the function operates correctly:
   ```
   VERTEX_PROJECT_ID=
   APP_BUILDER_PROJECT_ID=
   SEARCH_ENGINE=
   ENGINE_TYPE=
   ```

After running the above command, the function will be deployed and ready to handle requests.

## Notes

- Make sure to replace `ai-nativeframework` with your Google Cloud project ID if it differs.
- The region `us-east1` is used in the deployment command; you may choose a different region that is closer to your users or meets your latency requirements.
- Environment variables can be set in the Google Cloud Console under the 'Environment variables' section of your function's settings.

