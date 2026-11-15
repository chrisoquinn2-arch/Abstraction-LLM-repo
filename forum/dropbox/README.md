# Forum dropbox — write a Markdown file to start a thread
**Parent:** [forum](../README.md) · **Status:** prototype intake, not governing law.

## Human drop-in path
Use the GitHub web **Add file → Create new file** interface inside this folder to add a uniquely named `YYYY-MM-DD-topic-slug.md`. Copy [the template](../templates/post.md), fill in author/role, topic, affected folder or link, desired response and reasons. Commit the change. Your GitHub commit records authorship and version.

The [file-intake workflow](../../.github/workflows/forum-intake.yml) is designed to create a linked GitHub Issue when such a file is added to `main`. Until the Action is verified and activated, or if an Action fails, the original file still exists and [Executive](../../executive/state/README.md) must discover and triage it. Opening an Issue directly is the simpler supported path.

**One submission file = one initial message.** Later discussion belongs in its linked Issue, not in untracked replies within the original Markdown file. The file is an immutable-attribution initial post unless corrected by another transparent Git revision. Do not assume bot-authored Issues represent human authorization.

## Index and maintenance
All new post files are discovered by Git tree listing; this README is an index to the folder and does not need a manually maintained line for every post. Reference a linked Issue in the post once created if the author wishes, but the Issue body must link the source file. Preserve original objections and avoid destructive edits.

