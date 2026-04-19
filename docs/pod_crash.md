Title: Pod CrashLoopBackOff Troubleshooting

Steps:
1. Check pod status:
   kubectl get pods

2. Describe pod:
   kubectl describe pod <pod-name>

3. Check logs:
   kubectl logs <pod-name>

4. Look for:
   - OOMKilled
   - CrashLoopBackOff
   - ImagePullError

5. Fix:
   - Increase memory limits
   - Fix application errors
   - Restart deployment