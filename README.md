# Demo objective

Very simple demo to highlight the use of the PHI and MISTRAL APIs using the Azure AI Inference SDK and switch between the models with no code changes.

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

This demo is best served in debug more.

1. The project is set up to run in GitHub Codespaces. From [ai-tour-maas-demo-1](https://github.com/gloveboxes/ai-tour-maas-demo-1), select **<> Code** and then **Open with Codespaces**.
2. Open the `main.py` file.
3. Set a breakpoint at the line where the model is loaded at `client = ChatCompletionsClient(`.
4. Set a breakpoint at the line `model_info = client.get_model_info()` to see the model information.
5. Press F5 to start the debug session.
6. Single step through the code to see the model info and the completion results.
7. Uncomment the `# endpoint, key = config.get("mistral")` line to switch models and rerun the demo.


