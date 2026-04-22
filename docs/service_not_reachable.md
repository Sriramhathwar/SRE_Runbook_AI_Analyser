Title: Kubernetes Service Not Reachable

Steps:
1. Check service:
   kubectl get svc

2. Describe service:
   kubectl describe svc <name>

3. Verify endpoints:
   kubectl get endpoints <service-name>

4. Check pod labels:
   kubectl get pods --show-labels

5. Test connectivity:
   curl <service-ip>:<port>

Fix:
- Match labels with selectors
- Ensure pods are running
- Check network policies