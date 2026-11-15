"""Unit tests for file-native structural verification; not governance integration tests."""
import tempfile
import unittest
from pathlib import Path

from tools.institution_audit import check, links_from_text


class StructuralAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "CHARTER.md").write_text("# Charter\n")
        (self.root / "README.md").write_text("# Root\n\nMaintenance is required.\n")
        forms = self.root / ".github" / "ISSUE_TEMPLATE"
        forms.mkdir(parents=True)
        (self.root / ".github" / "README.md").write_text(
            "# GitHub\n\nMaintenance.\n\n[Forms](ISSUE_TEMPLATE/README.md)\n")
        (forms / "README.md").write_text("# Forms\n\nMaintenance rules.\n")
        for name in ("discussion.yml", "challenge.yml", "work.yml"):
            (forms / name).write_text("name: N\ndescription: D\nbody:\n")
        (self.root / "README.md").write_text(
            "# Root\n\nMaintenance.\n\n[Configuration](.github/README.md)\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_valid_minimal_tree(self):
        self.assertEqual(check(self.root), [])

    def test_missing_subfolder_readme(self):
        (self.root / "research").mkdir()
        (self.root / "research" / "study.md").write_text("# Study\n")
        self.assertTrue(any("research: missing README" in x for x in check(self.root)))

    def test_unindexed_subfolder(self):
        d = self.root / "research"
        d.mkdir()
        (d / "README.md").write_text("# Research\n\nMaintenance of context.\n")
        self.assertTrue(any("does not index research/README" in x for x in check(self.root)))

    def test_broken_link(self):
        with (self.root / "README.md").open("a") as out:
            out.write("\n[Missing](nowhere.md)\n")
        self.assertTrue(any("broken local link" in x for x in check(self.root)))

    def test_decision_without_status(self):
        d = self.root / "governance" / "decisions"
        d.mkdir(parents=True)
        (self.root / "governance" / "README.md").write_text(
            "# Governance\n\nMaintenance.\n\n[Decisions](decisions/README.md)\n")
        (d / "README.md").write_text("# Decisions\n\nMaintenance.\n")
        (d / "adr.md").write_text("# An unexplained rule\nAuthority: agent\n")
        with (self.root / "README.md").open("a") as out:
            out.write("\n[Governance](governance/README.md)\n")
        self.assertTrue(any("decision needs explicit Status" in x for x in check(self.root)))

    def test_markdown_fences_are_not_active_links(self):
        contents = "See [valid](./README.md)\n```\n[bad](missing.md)\n```\n"
        self.assertEqual(links_from_text(contents), ["./README.md"])

    def test_bad_dropbox_post(self):
        d = self.root / "forum" / "dropbox"
        d.mkdir(parents=True)
        (self.root / "forum" / "README.md").write_text(
            "# Forum\n\nMaintenance.\n\n[Drop](dropbox/README.md)\n")
        (d / "README.md").write_text("# Inbox\n\nMaintenance.\n")
        (d / "undated.md").write_text("# Hello\n")
        with (self.root / "README.md").open("a") as out:
            out.write("\n[Forum](forum/README.md)\n")
        self.assertTrue(any("use dated slug naming" in x for x in check(self.root)))


if __name__ == "__main__":
    unittest.main()

