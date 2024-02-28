from datasurface.md.Governance import Ecosystem


def createEcosystem() -> Ecosystem:
    return Ecosystem("test", GithubRepository("test", "owner", "repo")
                     )
