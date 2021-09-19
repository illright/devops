# Kubernetes report

Note: both the service and the deployment can be found in the respective app's YAML config in this directory.

1 replica:

```
❭ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-65f7f9b645-gkntp   1/1     Running   0          91s

NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/app-python-service   LoadBalancer   10.99.57.107   <pending>     80:30000/TCP   20h
service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP        22h
```

3 replicas:

```
❭ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-65f7f9b645-cgwz2   1/1     Running   0          62s
pod/app-python-65f7f9b645-ck9zg   1/1     Running   0          62s
pod/app-python-65f7f9b645-sjjqc   1/1     Running   0          62s

NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/app-python-service   LoadBalancer   10.99.162.38   <pending>     80:30000/TCP   58s
service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP        22h
```

## Kubernetes concepts

### Ingress

An ingress is a set of routing rules used by the ingress controller to route external requests to destination pods. The rules map a hostname and a URL path to a particular service within the cluster.

### Ingress controller

An application inside the Kubernetes cluster that performs the actual routing in accordance to the ingresses defined within the cluster. This application lives in a separate pod.

### Stateful set

A means of deploying stateful applications in the cluster. Unlike the Deployment, the pods created by the Stateful Set will not be interchangeable, one of the pods will be assigned as the master and the others will simply replicate its behaviour.

### Daemon set

A means of ensuring that every single node in a cluster has a particular pod running. When new nodes will enter the cluster, the Daemon Set will add its pod into it. This is useful for sattelite applications like health monitors.

### Persistent volume

An abstraction over a storage medium (can be anything from a local drive to a cloud-based store) that specifies the properties of that storage (its size, access control, access speed, etc.). The applications can then persist their data in these volumes by claiming them with Persistent Volume Claims.
