Title: Persistent Volume Mount Issue

Steps:
1. Check PVC:
   kubectl get pvc

2. Describe PVC:
   kubectl describe pvc <name>

3. Check PV:
   kubectl get pv

4. Check pod events:
   kubectl describe pod <pod-name>

Fix:
- Ensure PV bound to PVC
- Check storage class
- Verify permissions