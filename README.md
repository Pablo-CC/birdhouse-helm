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

