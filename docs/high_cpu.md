Title: High CPU Usage in Kubernetes

Steps:
1. Check node usage:
   kubectl top nodes

2. Check pod usage:
   kubectl top pods

3. Identify high CPU pods

4. Fix:
   - Scale deployment
   - Optimize application
   - Increase resources