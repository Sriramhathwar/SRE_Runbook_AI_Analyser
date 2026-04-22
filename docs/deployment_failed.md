Title: Kubernetes Deployment Rollout Failure

Steps:
1. Check rollout status:
   kubectl rollout status deployment <name>

2. Describe deployment:
   kubectl describe deployment <name>

3. Check replica sets:
   kubectl get rs

4. Check pod logs:
   kubectl logs <pod-name>

5. Look for:
   - ImagePullBackOff
   - CrashLoopBackOff
   - Readiness probe failure

Fix:
- Correct image version
- Fix container startup errors
- Adjust readiness/liveness probes