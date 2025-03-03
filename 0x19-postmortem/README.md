 Service Outage Due to Database Connection Pool Exhaustion
Issue Summary
Duration: October 5, 2023, 14:30 UTC to 19:15 UTC (4 hours 45 minutes).
Impact: 30% of users experienced login failures and delayed dashboard loading. The Authentication API and User Profile Service were degraded.
Root Cause: A misconfigured database connection pool limit in a deployment caused pool exhaustion, leading to cascading failures.
Timeline
14:30 UTC: Deployment of v2.1.3 to the User Profile Service completed.
14:35 UTC: Issue detected via a surge in database latency alerts (threshold: 95th percentile > 2s).
14:40 UTC: Engineering team began investigating database health, suspecting hardware/resource constraints. Queries per second (QPS) were abnormally high.
15:00 UTC: Assumed network congestion; reviewed load balancer metrics but found no anomalies.
15:30 UTC: Escalated to the Database Team to inspect query performance and index usage. No slow queries identified.
16:15 UTC: Noticed connection pool saturation logs. Misleadingly attributed this to a transient traffic spike and restarted database nodes, temporarily reducing errors.
17:00 UTC: Errors resurged. Incident escalated to DevOps to audit the v2.1.3 deployment.
18:10 UTC: Identified the connection pool configuration error (max connections reduced from 200 to 20 in error).
19:15 UTC: Rolled back deployment to v2.1.2, restoring normal operations.
Root Cause and Resolution
Root Cause: A deployment script erroneously set the database connection pool’s max_connections parameter to 20 (down from 200) due to a typo in the configuration file (pool_config.yml). This caused threads to stall waiting for connections, leading to timeouts and HTTP 503 errors.
Resolution: The faulty deployment was rolled back, reverting the connection pool settings. Full service recovery was confirmed after 10 minutes of monitoring post-rollback.
Corrective and Preventative Measures
Improvements:
Strengthen pre-deployment validation for critical configuration parameters.
Enhance monitoring to detect connection pool saturation proactively.
Reduce reliance on manual rollbacks through automation.
Tasks:
Update CI/CD pipeline to validate connection pool settings against a baseline during deployment.
Add real-time alerts for connection pool usage exceeding 80% capacity.
Develop an automated rollback script triggered by health-check failures post-deployment.
Conduct a workshop on configuration management best practices for DevOps engineers.
Implement integration tests simulating traffic spikes to uncover resource bottlenecks.

