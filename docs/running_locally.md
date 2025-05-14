# Running Fission Functions Locally

1. Go to `schema_manager` project and setup the db and migrations properly by reading the `README` file

2. Go the respective service that you want to run. For example: `<service-name>_service`


3. Deploying to the local kind cluster

    ``` bash
    ./deploy.sh <service-name>
    ```

    For example:

    ```bash
    ./deploy.sh access_management
    ```

4. To test the fission function run this command

    ```bash
    fission function test --name <function-name> -v=2
    ```

    > ***Note***: If you want to test the function with payload and different http method then you need to pass --method and --body flags.Refer to the `fission function test` document [here](https://fission.io/docs/reference/fission-cli/fission_function_test/).

5. To check the fission function logs

    ```bash
    fission function log --name <function-name> -v=2
    ```
