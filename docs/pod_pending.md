Title: Pod Stuck in Pending State

Steps:
1. Check pod:
   kubectl get pods

2. Describe pod:
   kubectl describe pod <pod-name>

3. Look for:
   - Insufficient CPU/memory
   - Node selector mismatch

4. Check nodes:
   kubectl get nodes

Fix:
- Add resources to cluster
- Adjust resource requests
- Fix node selectors