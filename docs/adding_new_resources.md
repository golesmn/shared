
# Creating Resources in fission


## Create Resources with `--spec`

When creating Fission resources, use the `--spec` flag to generate corresponding YAML files in the `specs/` directory. For example:

```bash
# Create an environment
fission env create --name python --image fission/python-env --spec

# Create a function
fission function create --name hello --env python --code hello.py --spec

# Create an HTTP trigger
fission httptrigger create --name hello-trigger --function hello --url /hello --method GET --spec
```

Each command generates a YAML file in the `specs/` directory representing the resource.

---

## Apply the Spec to Your Cluster

> ***Note***: We have already automated this step in `deploy.sh` file. This is just for reference.

After defining your resources, apply them to your Kubernetes cluster:

```bash
fission spec apply --wait
```

This command performs the following actions:

* **Create** resources defined in the spec that don't exist in the cluster.
* **Update** existing resources in the cluster to match the spec.
* **Delete** resources in the cluster that were previously applied via spec but are no longer present in the current spec.

For continuous deployment, you can use:

```bash
fission spec apply --watch
```

This command watches for changes in the `specs/` directory and applies them automatically.

---

## Example: Adding a New Function via Spec

1. Initialize the spec directory:

```bash
fission spec init
```

2. Create a new environment:

```bash
fission env create --name nodejs --image fission/node-env --spec
```

3. Create a new function:

```bash
fission function create --name greet --env nodejs --code greet.js --spec
```

4. Create an HTTP trigger:

```bash
fission httptrigger create --name greet-trigger --function greet --url /greet --method GET --spec
```

5. Apply the spec:

```bash
fission spec apply --wait
```

Your new function is now deployed and accessible via the specified HTTP trigger.

---

## 🛠️ Tips

* **Version Control**: Store your `specs/` directory in version control to track changes and collaborate with your team.
* **CI/CD Integration**: Incorporate `fission spec apply` into your CI/CD pipelines for automated deployments.
* **Customization**: You can manually edit the YAML files in the `specs/` directory for advanced configurations.

For more detailed information, refer to the [Fission Spec Documentation](https://fission.io/docs/usage/spec/).