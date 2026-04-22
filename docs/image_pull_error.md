Title: ImagePullBackOff Issue

Steps:
1. Describe pod:
   kubectl describe pod <pod-name>

2. Check image name:
   Verify correct image and tag

3. Check registry access:
   docker pull <image>

4. Verify secrets:
   kubectl get secrets

Fix:
- Correct image name
- Add imagePullSecrets
- Check registry authentication