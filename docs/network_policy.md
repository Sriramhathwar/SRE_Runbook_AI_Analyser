Title: Network Policy Blocking Traffic

Steps:
1. Check policies:
   kubectl get networkpolicy

2. Describe policy:
   kubectl describe networkpolicy

3. Test connectivity:
   curl between pods

Fix:
- Update allow rules
- Add ingress/egress rules