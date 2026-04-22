Title: Kubernetes API Server Not Responding

Steps:
1. Check cluster:
   kubectl cluster-info

2. Check API server:
   kubectl get componentstatuses

3. Check logs:
   journalctl -u kube-apiserver

Fix:
- Restart API server
- Check certificates
- Verify etcd health