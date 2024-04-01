# FIBRAS GenAI Chatbot

This document serves as a comprehensive guide for setting up and deploying the Fibras GenAI Chatbot, a React-based project that integrates seamlessly with Google Cloud Platform (GCP) for the utilization of Cloud Functions. Designed to enhance user engagement through conversational AI, the Fibras GenAI Chatbot leverages the dynamic capabilities of React for the frontend and the robust infrastructure of GCP for backend processes, ensuring a smooth and responsive user experience.

## Getting Started

Before diving into the deployment process, ensure you have the following prerequisites installed and set up on your system:

- Node.js (v16.20.2 recommended)
- npm (comes with Node.js)
- Google Cloud SDK (gcloud CLI)
- Docker, Podman, or similar containerization tools

This project uses Node Version Manager (NVM) to manage Node versions. It's recommended to use Node v16.20.0 for compatibility.

## Setting Up the Project

1. Clone the repository to your local machine.
2. Navigate to the project directory and run `npm install` to install all the necessary dependencies.
3. To start the development server, run:
   ```
   npm start
   ```
   This will launch the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

## Deploying to Google Cloud Platform (GCP)

To update the deployment of the Fibras GenAI Chatbot, follow these steps:

1. Run the full deployment command:
   ```
   npm run full:deploy
   ```
   This command builds the React App, builds the Docker image, submits it to Google Cloud Build, and then deploys it to Cloud Run.

2. When prompted for the Service name, the default (`fibras-front`) is used. Simply press Enter to continue.

3. For the region selection, when prompted `Please specify a region:`, enter `33` to select `[33] us-east1`.

After the deployment process completes, you can verify the deployment in the Google Cloud Platform Console at:
[https://console.cloud.google.com/run/detail/us-east1/fibras-front/revisions?project=ai-nativeframework](https://console.cloud.google.com/run/detail/us-east1/fibras-front/revisions?project=ai-nativeframework)

The project is currently deployed and accessible at the following URL:
[https://fibras-front-7z6id7bqna-ue.a.run.app](https://fibras-front-7z6id7bqna-ue.a.run.app)


## GCP Webhooks Folder

The `/GCP_Webhooks` folder contains Cloud Functions that are integral to the project's backend. Each function within this folder has its own README file detailing its purpose, functionality, and deployment process. Refer to these READMEs for more information on managing and deploying these functions.

## Additional Information

For more details on React and how to work with Create React App, visit the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn more about deploying applications to GCP, refer to the [Google Cloud documentation](https://cloud.google.com/docs).

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests or issues as needed.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
