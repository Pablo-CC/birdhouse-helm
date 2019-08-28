# Birdhouse Helm Chart
This Helm Chart installs some of the components of the [Birdhouse project](https://birdhouse.readthedocs.io/en/latest/) into a Kubernetes cluster.
In this deployment [Phoenix](https://pyramid-phoenix.readthedocs.io/en/latest/) acts as the WPS web-based client to [Emu](https://emu.readthedocs.io/en/latest/), [Hummingbird](https://birdhouse-hummingbird.readthedocs.io/en/latest/), [FlyingPigeon](https://flyingpigeon.readthedocs.io/en/latest/) or other WPS you may want to deploy and register into Phoenix.

![phoenix](screenshot.png)
## TL;DR
```
git clone https://github.com/Pablo-CC/birdhouse-helm.git
kubectl create namespace birdhouse
helm install --name birdhouse --namespace birdhouse .
```
## Configuration

| Parameter                                       | Description                                                                                                        | Default                                                                                                                                   |
| ---                                             | ---                                                                                                                | ---                                                                                                                                       |
| `phoenix.name`                                  | The name for the phoenix deployment                                                                                | `phoenix`
| `phoenix.image`                                 | The image for the phoenix container                                                                                | `birdhouse/pyramid-phoenix`
| `phoenix.imagePullPolicy`                       | The image pull policy                                                                                              | `IfNotPresent`
| `phoenix.replicas`                              | The number of Phoenix's replicas for the deployment to build                                                       | `1`
| `phoenix.hostname`                              | The FQDN of Phoenix [\*]                                                                                           | ``
| `phoenix.ports.http`                            | The port to listen on for HTTP requests                                                                            | `8081`
| `phoenix.ports.https`                           | The port to listen on for HTTPS requests                                                                           | `8443`
| `phoenix.mongodb.name`                          | The name for the deployment of the MongoDB instance                                                                | `mongoldb`
| `phoenix.mongodb.port`                          | The port that MongoDB listens on                                                                                   | `27017`
| `phoenix.mongodb.image`                         | The image for the MongoDB container                                                                                | `mongo:2.6.12`
| `phoenix.mongodb.imagePullPolicy`               | The image pull policy                                                                                              | `IfNotPresent`
| `phoenix.resources.requests.memory`             | The minimum memory requests for Phoenix (required for HPA on Memory usage)                                         | `1Gi`
| `phoenix.resources.requests.cpu`                | The minimum CPU request for Phoenix (required for HPA on CPU usage)                                                | `400m`
| `phoenix.hpa.enabled`                           | Boolean for enabling Horizontal Pod Autoscaling for Phoenix                                                        | `true`
| `phoenix.hpa.minReplicas`                       | The minimum number of replicas for the Autoscaler                                                                  | `1`
| `phoenix.hpa.maxReplicas`                       | The maximum number of replicas for the Autoscaler                                                                  | `8`
| `phoenix.hpa.cpuUtilization`                    | Autoscaling trigger as a percentage of `phoenix.resources.requests.cpu`                                            | `80`
| `phoenix.hpa.memUtilization`                    | Autoscaling trigger as a percentage of `phoenix.resources.requests.memory`                                         | `100`
| `phoenix.emu.enabled`                           | Boolean for enabling EMU as a backend Web Processing Service                                                       | `true`
| `phoenix.emu.name`                              | The name for the Emu Deployment                                                                                    | `emu`
| `phoenix.emu.image`                             | The image for Emu's container                                                                                      | `birhouse/emu`
| `phoenix.emu.imagePullPolicy`                   | The image pull policy                                                                                              | `IfNotPresent`
| `phoenix.emu.replicas`                          | The number of Emu's replicas for the deployment to build                                                           | `1`
| `phoenix.emu.hostname`                          | The FQDN of Emu [*]                                                                                                | ``
| `phoenix.emu.port`                              | The port on which Emu listens                                                                                      | `5000`
| `phoenix.emu.logLevel`                          | The log level for Emu [DEBUG, INFO, WARN, ERROR]                                                                   | `WARN`
| `phoenix.flyingpigeon.enabled`                  | Boolean for enabling FlyingPigeon as a backend Web Processing Service                                              | `true`
| `phoenix.flyingpiugeon.name`                    | The name for the FlyingPigeon deployment                                                                           | `flyingpigeon`
| `phoenix.flyingpigeon.image`                    | The image for FlyingPigeon's container                                                                             | `birdhouse/flyingpigeon`
| `phoenix.flyingpigeon.imagePullPolicy`          | The image pull policy                                                                                              | `IfNotPresent`
| `phoenix.flyingpigeon.replicas`                 | The number of FlyingPigeon's replicas for the deployment to build                                                  | `1`
| `phoenix.flyingpigeon.hostname`                 | The FQDN of FlyingPigeon                                                                                           | ``
| `phoenix.flyingpigeon.port`                     | The port on which FlyingPigeon listens                                                                             | `5000`
| `phoenix.flyingpigeon.logLevel`                 | The log level for FlyingPigeon [DEBUG, INFO, WARN, ERROR]                                                          | `WARN`
| `phoenix.hummingbird.enabled`                   | Boolean for enabling Hummingbird as a backend Web Processing Service                                               | `true`
| `phoenix.hummingbird.name`                      | The name for the Hummingbird deployment                                                                            | `hummingbird`
| `phoenix.hummingbird.image`                     | The image for Hummingbird's container                                                                              | `birdhouse/hummingbird`
| `phoenix.hummingbird.imagePullPolicy`           | The image pull policy                                                                                              | `IfNotPresent`
| `phoenix.hummingbird.replicas`                  | The number of Hummingbird's replicas for the deployment to build                                                   | `1`
| `phoenix.hummingbird.hostname`                  | The FQDN of FlyingPigeon                                                                                           | ``
| `phoenix.hummingbird.port`                      | The port on which Hummingbird listens                                                                              | `5000`
| `phoenix.hummingbird.logLevel`                  | The log level for Emu [DEBUG, INFO, WARN, ERROR]                                                                   | `WARN`
|

[*] *Tip: You can use [nip.io](https://nip.io/)*


Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,

```bash
$ helm install --name my-release --namespace birdhouse --set emu.enabled=false .
```

Alternatively, a YAML file that specifies the values for the parameters can be provided while installing the chart. For example,

```bash
$ helm install --name my-release -f my_values.yaml .
```

## Autoscaling
Kubernetes' Horizontal Pod Autoscaler is used for the autoscaling of the frontend (i.e. Phoenix). The following figures represent the results of this during a load test:

### CPU Usage
![cpu_usage.png](./plot_hpa/cpu_usage.png)
### Memory Usage
![memory_usage.png](./plot_hpa/memory_usage.png)
### Replicas + Requests
![replicas_and_requests.png](./plot_hpa/replicas_and_requests.png)
### Replicas
![num_of_replicas.png](./plot_hpa/num_of_replicas.png)
### Requests per second
![req_per_sec.png](./plot_hpa/req_per_sec.png)

