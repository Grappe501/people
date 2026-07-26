# People Intake — UX Acceptance Tests and Edge Cases

**Status:** draft_complete  
**Version:** 1.0  
**Build:** PEOPLE-WORKFLOW-UX-DESIGN-1.0  
**Companion to:** Workflow + UX volume

---

## UX Acceptance Tests

### Field Uploader

1. Sign in  
2. Start a batch  
3. Photograph five pages  
4. Review them  
5. Upload them  
6. Confirm completion  

Without training beyond in-app guidance.

### Data Entry

1. Sign in  
2. Claim a page  
3. Zoom the image  
4. Enter seven people  
5. Correct one entry  
6. Mark one field unreadable  
7. Submit the page  
8. Automatically open the next page  

### Reviewer

1. Open a possible match  
2. Understand why it was suggested  
3. Compare values  
4. Link or create  
5. Resolve field conflicts  
6. Complete the entry  

### Administrator

1. Find a stuck page  
2. Identify the assigned user  
3. Release or reassign the claim  
4. Preserve the existing draft  
5. View the audit history  

---

## Critical Edge Cases (Must Be Handled)

1. Page with no entries  
2. Page with one entry  
3. Page with ten entries  
4. More than ten handwritten lines  
5. Two people with the same name  
6. Shared household phone  
7. Shared household email  
8. No phone or email  
9. Illegible name  
10. Illegible individual field  
11. Duplicate image uploaded twice  
12. Same sheet uploaded in separate batches  
13. Page uploaded sideways  
14. Image cut off  
15. Data-entry user closes app  
16. Data-entry user loses connection  
17. Claim expires  
18. Administrator reassigns work  
19. Reviewer disagrees with suggested match  
20. New intake conflicts with existing person data  
21. User submits the same page twice  
22. Batch upload only partially succeeds  
23. Page entered against wrong image  
24. Row values accidentally shifted  
25. Existing person already has multiple emails or phones  
26. Page returned after matching begins  
27. Completed page must be corrected  
28. User access disabled mid-session  
29. Signed image URL expires  
30. Batch remains inactive for an extended period  

Detailed handling lives in exception, queue, transcription, and matching workflow docs. Data-layer resolution of multi-email/phone is deferred.
