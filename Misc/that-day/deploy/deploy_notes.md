## Install microk8s
1. Update repository

```
sudo apt update
```

2. Install microk8s

```
sudo snap install microk8s --classic
```

3. Check the status while Kubernetes starts
```
microk8s status --wait-ready

sudo usermod -a -G microk8s ubuntu

sudo chown -R ubuntu ~/.kube

// if need to enable service
microk8s enable --help
```

4. Start using Kubernetes
```
alias k="microk8s kubectl"
k get all --all-namespaces
```

5. Enable service
```
<!-- CoreDNS -->
microk8s enable dns

<!-- RBAC -->
microk8s enable rbac

<!-- Local Storage -->
microk8s enable hostpath-storage

<!-- Ingress -->
microk8s enable ingress
```

6. Enable anonymous auth
```
sudo vim /var/snap/microk8s/6809/args/kubelet
--> anonymous-auth=true

sudo systemctl restart snap.microk8s.daemon-kubelite.service
```

## Put sites to /var/www/sites

