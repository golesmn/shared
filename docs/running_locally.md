# Running Fission Functions Locally

1. Go the respective service that you want to run. For example: `access_management_service`
2. fission spec apply --wait -v=2
3. This should deploy all the required fission resources to the cluster
4. To test the fission function run this 

```bash

fission function test --name <function-name> -v=2

```

Note: function names can be listed with command
```bash 
fission function list
```
