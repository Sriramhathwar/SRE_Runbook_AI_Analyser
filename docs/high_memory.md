Title: High Memory Usage in Cluster

Steps:
1. Check node usage:
   kubectl top nodes

2. Check pod usage:
   kubectl top pods

3. Identify high memory pods

Fix:
- Scale deployment
- Optimize application
- Increase memory limits