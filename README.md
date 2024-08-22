# Demo objective

This demo showcases how to use the PHI and MISTRAL APIs with the Azure AI Inference SDK, allowing you to switch between models without changing the code.

### GitHub Codespaces

You can run this template virtually by using GitHub Codespaces. The button will open a web-based VS Code instance in your browser:

1. Open the template (this may take several minutes):

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/gloveboxes/ai-tour-maas-demo-1)

### VS Code Dev Containers

A related option is VS Code Dev Containers, which will open the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1. Start Docker Desktop (install it if not already installed)
2. Open the project:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/gloveboxes/ai-tour-maas-demo-1)

## Demo set up

Set these two sets of environment variables before running the sample. The endpoint and key values can be found in the AI Studio portal.

1. Rename the `.env.sample` file to `.env`.
2. Add the following values to the `.env` file:

    ```bash
    PHI_ENDPOINT=<your_PHI_endpoint>
    PHI_KEY=<your_PHI_key>
    MISTRAL_ENDPOINT=<your_MISTRAL_endpoint>
    MISTRAL_KEY=<your_MISTRAL_key>
    ```

## Demo hints

- This demo is best served in debug mode.
- Be sure to create your Codespace before the demo as it'll take a minute or two to set up.

Follow these steps:

1. The project is set up to run in GitHub Codespaces. From [ai-tour-maas-demo-1](https://github.com/gloveboxes/ai-tour-maas-demo-1), select **<> Code** and then **Open with Codespaces**.
2. Open the `main.py` file.
3. Set the following breakpoints:
   1. At `endpoint, key = config.get("phi")` to see the PHI model information. But don't show the key:)
   2. At the line where the model is loaded at `client = ChatCompletionsClient(`.
   3. At `model_info = client.get_model_info()` to see the model information.
4. Press F5 to start the debug session.
5. Single step through the code to see the model info and the completion results.
6. Uncomment the `# endpoint, key = config.get("mistral")` line to switch models and rerun the demo.
