# People Intake — Security Testing Requirements

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-SECURITY-API-ENGINEERING-DESIGN-1.0  
**Companion:** Threat model + authz matrix

Future implementation must prove:

1. Unapproved account denied  
2. Disabled user denied  
3. Uploader cannot access unrelated image  
4. Data-entry cannot browse candidate people  
5. Reviewer cannot manage users  
6. Admin cannot assign owner role  
7. User cannot alter role in browser  
8. User cannot access page by guessed ID  
9. Expired signed image URL fails  
10. Public object access fails  
11. Unsupported file rejected  
12. Malicious file disguised as image rejected  
13. Duplicate submission idempotent  
14. Stale page update rejected  
15. Expired claim cannot save over new claim  
16. Match cannot resolve twice  
17. Person promotion cannot duplicate on retry  
18. Logs contain no raw PII  
19. Error responses contain no secrets  
20. Production startup fails when required secrets absent  
21. Application credential cannot run migrations  
22. Application cannot write unrelated RedDirt tables  
23. Audit created for administrative override  
24. Unauthorized export route does not exist  
25. Disabled user’s active claim handled safely  

Full test catalog deferred to quality/ops freeze design.
