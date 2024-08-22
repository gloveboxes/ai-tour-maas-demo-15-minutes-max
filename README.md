# Demo objective

Very simple demo to highlight the use of the PHI and MISTRAL APIs using the Azure AI Inference SDK and switch between the models with no code changes.

## Demo hints

This demo is best served in debug more.

1. The project is set up to run in GitHub Codespaces. You can also run it locally.
1. Set a breakpoint at the line where the model is loaded at `client = ChatCompletionsClient(`
1. Set a breakpoint at the line `model_info = client.get_model_info()` to see the model information.
1. Single step through the code to see the model info and the completion results.
1. Uncomment the `# endpoint, key = config.get("mistral")` line to switch models and rerun the demo.

## Environment variables

Set these two sets of environment variables before running the sample. The endpoint and key values can be found in the AI Studio portal.

```bash
PHI_ENDPOINT=<your_PHI_endpoint>
PHI_KEY=<your_PHI_key>
MISTRAL_ENDPOINT=<your_MISTRAL_endpoint>
MISTRAL_KEY=<your_MISTRAL_key>
```
