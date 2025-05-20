# model-service

Wrapper service for the released ML model that has a REST API to expose the model to the other components.

1. To run the model-service locally use the following command:
    ```bash
    python3 app.py
    ```

2. Go to http://127.0.0.1:5050/test and you should see: 
    ```
    status: "Model-service is running"
    ```
