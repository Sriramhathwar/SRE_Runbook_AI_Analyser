Title: Node Not Ready Issue

Steps:
1. Check nodes:
   kubectl get nodes

2. Describe node:
   kubectl describe node <node-name>

3. Check kubelet:
   systemctl status kubelet

4. Fix:
   - Restart kubelet
   - Check disk pressure
   - Check network