Title: Pod OOMKilled (Out of Memory)

Steps:
1. Check pod status:
   kubectl get pods

2. Describe pod:
   kubectl describe pod <pod-name>

3. Check events:
   Look for OOMKilled

4. Check resource limits:
   kubectl describe pod <pod-name>

Fix:
- Increase memory limits
- Optimize application memory usage
- Add resource requests/limits