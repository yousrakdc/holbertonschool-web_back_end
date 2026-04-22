#!/usr/bin/env python3

"""Unittests and integration tests for client module."""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unittests for GithubOrgClient class."""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method."""
        expected = {"name": org_name}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url property."""
        repos_url = "https://api.github.com/orgs/google/repos"
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {"repos_url": repos_url}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, repos_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method."""
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        repos_url = "https://api.github.com/orgs/google/repos"

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_url:
            mock_public_url.return_value = repos_url

            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_public_url.assert_called_once()
            mock_get_json.assert_called_once_with(repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license static method."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected,
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up patched requests.get for integration tests."""
        cls.org_name = cls._extract_org_name(cls.org_payload)
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            response = Mock()
            if url == GithubOrgClient.ORG_URL.format(org=cls.org_name):
                response.json.return_value = cls.org_payload
            elif url == cls.org_payload.get("repos_url"):
                response.json.return_value = cls.repos_payload
            else:
                response.json.return_value = {}
            return response

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patched requests.get."""
        cls.get_patcher.stop()

    @staticmethod
    def _extract_org_name(org_payload):
        """Extract org name from repos_url structure."""
        if not org_payload:
            return ""
        if org_payload.get("login"):
            return org_payload["login"]
        repos_url = org_payload.get("repos_url", "")
        return repos_url.rstrip("/").split("/")[-2] if repos_url else ""
