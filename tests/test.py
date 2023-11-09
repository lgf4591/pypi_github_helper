from pypi_github_helper.github_helper import Github

if __name__ == "__main__":
    print(Github.gh_proxies)
    github = Github("MatsuriDayo/nekoray")
    print(github.download_urls)
