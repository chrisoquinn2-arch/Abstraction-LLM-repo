# Risk register for file-native prototype
**Status:** OPEN risks, not verified failures · **Authority:** design and test only, Charter outset task 1.

| ID | Risk | Observable test | Owner |
| --- | --- | --- | --- |
| R-F01 | Misrouted Issue receives no accountable substantive reply | Post wrong-domain discussion and check actual acknowledgments | Executive |
| R-F02 | Parent README becomes semantically stale | Change institutional structure without README and inspect CI + human review | Operations |
| R-F03 | Human browser edit is lost or creates an unindexed child | Open/edit/pr and verify parent, PR and source links | Operations |
| R-F04 | A normative PR merges without valid ratification | Attempt change under ambiguous authority and verify Governance blocks/enquires | Governance |
| R-F05 | Markdown dropbox post is not converted due to workflow limits | Merge test post; inspect GitHub Action and Issue; manual recovery when failure | Executive + Operations |
| R-F06 | Agents lose chat context or inaccessible connector state | Fresh instance given only repo and Issue URL; check recovery | Executive + Operations |
| R-F07 | GitHub Issue/PR and file state drift | Revise role or decision; inspect linked Issue and dependent files | Governance + Operations |
| R-F08 | Forum/Issue volume exceeds bounded agent context | Create many independent threads; evaluate missed/delayed items | Executive |
| R-F09 | Scientific claims get promoted due to social consensus | Synthetic challenge of provisional claim and check separate evidence review | Research |
| R-F10 | Human identity/attribution lost during bot conversion | Submit Markdown file; compare original Git author and resulting Issue | Operations |

**No test here is claimed passed.** Record observations, costs, exact revisions, human reviewer feedback and corrective design decisions in the relevant PR/Issue. This register is a reasoned starting hypothesis.

