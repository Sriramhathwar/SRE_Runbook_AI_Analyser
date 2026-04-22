Title: Kubernetes DNS Resolution Issue

Steps:
1. Exec into pod:
   kubectl exec -it <pod> -- sh

2. Test DNS:
   nslookup google.com

3. Check CoreDNS:
   kubectl get pods -n kube-system

4. Check logs:
   kubectl logs -n kube-system <coredns-pod>

Fix:
- Restart CoreDNS
- Check kube-dns config
- Verify network policies